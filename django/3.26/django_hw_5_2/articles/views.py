from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    article = Articles()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')