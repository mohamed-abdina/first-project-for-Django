from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('function/', views.hello_world, name='hello_world'),
    path('reservation/', views.reservation, name='reservation'),
]