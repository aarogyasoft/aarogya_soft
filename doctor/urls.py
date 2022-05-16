from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('doctor_dash', views.doctor_dash, name='doctor_dash'),
    path('update_patient_data', views.update_patient_data, name='update_patient_data'),
    path('view_patient_history', views.view_patient_history, name='view_patient_history')
]
