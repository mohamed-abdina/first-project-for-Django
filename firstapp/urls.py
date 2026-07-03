from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('function/', views.hello_world),
]