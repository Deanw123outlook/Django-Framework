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

def plot_type(chart_type, *args, **kwargs):
    # https://matplotlib.org/faq/usage_faq.html?highlight=backend#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(12,5))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    # barplot 
    if chart_type == 'bar':
        plt.style.use('ggplot')
        title = "Title"
        plt.title(title)
        plt.bar(x, y, color = 'r', alpha=0.65)
        print("bar-plot-executed")
    # lineplot
    elif chart_type == 'line':
        plt.style.use('ggplot')
        title = "Title"
        plt.title(title)
        plt.plot(x, y,color = 'g', alpha = 0.65)
        print("line-plot-executed")
    # scatterplot
    elif chart_type == 'scatter':
        plt.style.use('ggplot')
        title = 'Title'
        plt.title(title)
        plt.scatter(data,x, y,color=b, alpha = 0.65)
        print("scatter-plot-executed")
    # countplot
    else:
        sns.set_style('darkgrid')
        title = "Title"
        plt.title(title)
        sns.countplot(x, data)
        plt.tight_layout()
    # apply all charts
    plt.xticks(rotation=45)
    graph = get_image()
    return graph