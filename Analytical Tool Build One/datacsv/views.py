from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from products.models import Product, Purchase

# Create your views here.
def upload_file_view(request):
    success_message = None
    error_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        #
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                # Data Cleaning & Terminal Reading/Review
                for row in reader:
                    print("--------------csv-reader--------------")
                    print(row)
                    print(type(row))
                    row = "".join(row)
                    print(row)
                    row = row.replace(";"," ")
                    print(row)
                    row = row.split()
                    print(row)
                    #
                    user = User.objects.get(id=row[3])
                    print(user)
                    print("---------------------------------------")
                    # Populate Database
                    prod, _ = Product.objects.get_or_create(name=row[0])
                    Purchase.objects.create(
                        product=prod,
                        price = int(row[2]),
                        quantity = int(row[1]),
                        salesman = user,
                        date = row[4]+ " "+ row[5]
                        )

            obj.activated=True
            obj.save()
            success_message= "Uploaded sucessfully"
            print(success_message)
        except:
            error_message = "Ups. Something went wrong...."
            print(error_message)

        
    context = {
        'form':form,
        'success_message':success_message,
        'error_message':error_message,
    }
    return render(request, 'csv/upload.html', context)
