from django.urls import path
from .views import appointment, success

urlpatterns = [

    path(
        '',
        appointment,
        name='appointment'
    ),

    path(
        'success/',
        success,
        name='success'
    ),

]