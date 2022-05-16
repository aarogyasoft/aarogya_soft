from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.medicine_rec, name='medicine_rec')
]
