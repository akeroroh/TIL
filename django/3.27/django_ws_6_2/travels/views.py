from django.shortcuts import render, redirect
from .models import Travels
from .forms import TravelsForm

# Create your views here.
def index(request):
    travels = Travels.objects.all()
    context = {
        'travels': travels
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = TravelsForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelsForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def detail(request, travels_pk):
    travel = Travels.objects.get(pk=travels_pk)
    context = {
        'travel': travel
    }
    return render(request, 'detail.html', context)