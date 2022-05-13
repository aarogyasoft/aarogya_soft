from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('doctor_dash', views.doctor_dash, name='doctor_dash')
]
