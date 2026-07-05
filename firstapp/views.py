from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservationForm


def home(request):
    return HttpResponse("Home Page")


def hello_world(request):
    return HttpResponse("Hello World")


def reservation(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, 'reservation.html', {'form': form})