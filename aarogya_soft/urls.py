from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("index.urls")),
    path('index/', include("index.urls")),
    path('manage_data/', include("manage_data.urls")),
    path('admin/', admin.site.urls)
]
