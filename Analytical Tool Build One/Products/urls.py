from django.urls import path
from .views import chart_select_view, add_purchase_view, raw_data_analysis

# define app_name that matches namespace in root urls.py file
app_name = 'products'

urlpatterns = [
    path('', chart_select_view, name='main-products-view'),
    path('add/', add_purchase_view, name='add-purchase-view'),
    path('dataframe/', raw_data_analysis, name='dataframe-analysis-view')
]

# STEPS advised to take when starting project
# main urls -> app urls.py
# create view -> templates -> view to urls app