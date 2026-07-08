from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('appointments.urls')),   # Home page
    path('admin/', admin.site.urls),
    path('app/', include('appointments.urls')),
]