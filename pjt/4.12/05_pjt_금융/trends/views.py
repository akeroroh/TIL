from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from collections import Counter

def get_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    result_stats = soup.select_one("#result-stats")
    number = []
    for _ in result_stats.text:
        if _ == '개':
            break
        if _.isdigit():
            number.append(_)
    final_num = ''.join(number)
    return final_num

def get_data_year(keyword):
    url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    result_stats = soup.select_one('#result-stats')
    number = []
    for _ in result_stats.text:
        if _ == '개':
            break
        if _.isdigit():
            number.append(_)
    final_num = ''.join(number)
    return final_num

# Create your views here.
def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        form.save()
        return redirect('trends:keyword')
    else:
        form = KeywordForm()
    keywords = Keyword.objects.all()
    context = {
        'form': form,
        'keywords': keywords,
    }
    return render(request, 'keyword.html', context)

def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()
    
    for key in keywords:
        if not Trend.objects.filter(name=key.name):
            trend = Trend(name=key.name, result=int(get_data(key.name)), search_period='all')
            trend.save()
        else:
            trend = Trend.objects.get(name=key.name)
            trend.result = int(get_data(key.name))
            trend.save()
    
    trends = Trend.objects.all()
    context = {
        'trends': trends,
    }
    return render(request, 'crawling.html', context)

def crawling_histogram(request):
    plt.clf()
    trends  = Trend.objects.filter(search_period = 'all')
    bar_list = trends.values('name', 'result').all()
    
    for yoyo in bar_list:
        plt.bar(yoyo['name'], yoyo['result'])
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid(True)
    plt.rcParams['font.family'] ='Malgun Gothic'

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()

    for key in keywords:
        if not Trend.objects.filter(name=key.name, search_period='year'):
            trend = Trend(name=key.name, result=int(get_data_year(key.name)), search_period='year')
            trend.save()
        else:
            trend = Trend.objects.get(name=key.name, search_period='year')
            trend.result = int(get_data_year(key.name))
            trend.save()
    
    trends = Trend.objects.filter(search_period='year')
    bar_list = trends.values('name', 'result').all()

    for yoyo in bar_list:
        plt.bar(yoyo['name'], yoyo['result'])
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid(True)
    plt.rcParams['font.family'] ='Malgun Gothic'

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'crawling_advanced.html', context)
