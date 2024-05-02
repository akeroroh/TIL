from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurant_lst = Restaurant.objects.all()
    context = {
        'restaurant_lst': restaurant_lst
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    
    restaurant = Restaurant(name=name, description=description, address=address, phone_number=phone_number)
    restaurant.save()

    return redirect('restaurant:index')