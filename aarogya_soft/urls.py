from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("index.urls")),
    path('index/', include("index.urls")),
    path('patient/', include("patient.urls")),
    path('doctor/', include("doctor.urls")),
    path('admin/', admin.site.urls)
]
