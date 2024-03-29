from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservations/new.html', context)
        
def create(request):
    name = request.POST.get('name')
    date = request.POST.get('date')

    reservation = Reservation(name=name, date=date)
    reservation.save()
    return redirect('reservations:index')