from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .utils import get_plot
from .forms import PurchaseForm

# Create your views here.
def chart_select_view(request):
    graph = None
    error_message=None 
    df = None 
    price = None
    
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = product_df['id']
    
    # check if records exist in dataframe
    if purchase_df.shape[0] > 0:
        # Join df
        df = pd.merge(purchase_df,product_df, on='product_id').drop(['id_y','date_y'], axis=1).rename({'id_x':'id','date_x':'date'}, axis=1)
        price = df['price']
        # POST request (http) is used to send data to a server to create/update a resource
        if request.method == 'POST':
            print("--")
            print("request-type-testing")
            chart_type = request.POST.get('sales')
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            print(chart_type)
            print("--")
            #
            df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            df2 = df.groupby('date', as_index=True)['total_price'].agg('sum')
            
# --------------------------------CHART TYPE FUNCTIONALITY---------------------------------------#
            # bar chart
            if chart_type == "bar":
                if date_from != "" and date_to != "":
                    df = df[(df['date']>date_from) & (df['date']< date_to)]
                    print("--df-kerne--")
                    print(df.head())
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    print("--df2--")
                    print(df2.head(2))
                # function to get graph
                graph = get_plot(chart_type, x=df2['date'],y=df2['total_price'],data=df)
            
            # line plot
            elif chart_type == "line":
                if date_from != "" and date_to != "":
                    df = df[(df['date']>date_from) & (df['date']< date_to)]
                    print("--df-kerne--")
                    print(df.head())
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    print("--df2--")
                    print(df2.head(2))
                # function to get graph
                graph = get_plot(chart_type, x=df2['date'],y=df2['total_price'],data=df)
            
            # kernel density plot
            elif chart_type == "kernel":
                if date_from != "" and date_to != "":
                    df = df[(df['date']>date_from) & (df['date']< date_to)]
                    print("--df-kerne--")
                    print(df.head())
                # function to get graph
                graph = get_plot(chart_type, x=df['total_price'],y=df['date'],data=df)
            
            #
            elif chart_type == "pie": 
                if date_from != "" and date_to != "":
                    df = df[(df['date']>date_from) & (df['date']< date_to)]
                    print("--df-pie--")
                    print(df.head())
                    #
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    print("--df2-pie--")
                    print(df2.head())
                    #
                    df3 = df.groupby('name', as_index=False)['quantity'].agg('sum')
                    print("--df3-pie--")
                    print(df3)
                # function to get graph
                graph = get_plot(chart_type,y=df3['quantity'],labels=df3['name'],data=df3)
            
            # count plot  
            elif chart_type == "count":
                if date_from != "" and date_to != "":
                    df = df[(df['date']>date_from) & (df['date']< date_to)]
                    print("--df-kerne--")
                    print(df.head())
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    print("--df2--")
                    print(df2.head(2))
                # function to get graph
                graph = get_plot(chart_type, x=df2['date'],y=df2['total_price'],data=df)
                           
            else:
                error_message = 'Please select a chart type to continue'
                print(error_message)
    else:
        error_message = "No existing records in DATABASE/MODELS"
        df = None
     #
    context = {
        'graph':graph,
        'price':price,
        'error_message' :error_message,
        }
    # empty dictionary will hold content
    return render(request,'products/main.html',context)

# ADDING Purchases via FORM
def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message = None
    #
    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesman = request.user
        obj.save()
        #
        form = PurchaseForm()
        print("Form-Troubleshooting")
        added_message = "Data Added Succesfully"
        print(added_message)
    #
    context = {
        'form':form,
        'added_message':added_message,
    }
    return render(request,'products/add.html',context) # render() takes a request, a template, and a dictionary of context data and returns an HTTP response with the rendered HTML content.