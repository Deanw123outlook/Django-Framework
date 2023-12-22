import matplotlib.pyplot as plt 
import seaborn as sns
from io import BytesIO
import base64
from django.contrib.auth.models import User

def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file'
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    # free the memory of the buffer 
    buffer.close()
    return graph

def get_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/faq/usage_faq.html?highlight=backend#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    #
    if chart_type == 'bar':
        plt.style.use('ggplot')
        title = "Total Price Per Data (Bar Chart Analysis)"
        plt.title(title)
        plt.bar(x, y, color = 'r', alpha=0.65)
        print("bar-plot-executed")
    #
    elif chart_type == 'line':
        plt.style.use('ggplot')
        title = "Total Price Per Date"
        plt.title(title)
        plt.plot(x, y,color = 'g', alpha = 0.65)
        print("line-plot-executed")
    #
    elif chart_type =='kernel':
        plt.style.use('ggplot')
        title = "Total Price Kernel Density Plot Analysis"
        plt.title(title)
        sns.kdeplot(x,kde=True,hist=True,color='r')
    #
    elif chart_type == 'pie':
        plt.style.use('ggplot')
        title = "Product Quantity"
        plt.title(title)
        plt.pie(y)
        print("Revisit-Pie-Chart-Code!")
        print("Need-to-pull-in-lables")
    #
    else:
        plt.style.use('ggplot')
        title = "Total Product Count"
        plt.title(title)
        sns.countplot(data, x='name',color = 'b', alpha=0.65)
        print("count-plot-executed")
        
    # apply all charts
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph