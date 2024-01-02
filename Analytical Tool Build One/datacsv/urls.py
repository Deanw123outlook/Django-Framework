from django.urls import path
from .views import upload_file_view

# define app_name that matches namespace in root urls.py file
app_name = 'datacsv'

urlpatterns = [
    path('',upload_file_view, name='upload-view'),
]

# STEPS advised to take when starting project
# main urls -> app urls.py
# create view -> templates -> view to urls app