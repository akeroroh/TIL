from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries
    }
    return render(request, 'index.html', context)

def create(request):
    form = DiaryForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)