from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('upload_data', views.upload_data, name='upload_data'),
    path('view_data', views.view_data, name='view_data')
]
