from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import api_view
from .serializer import DepositOptionsSerializer, DepositProductsSerializer
from .models import DepositProducts, DepositOptions
import requests
from django.db import transaction
# Create your views here.

api_key = settings.API_KEY
BASE_URL='http://finlife.fss.or.kr/finlifeapi/'

def index(request):
    url = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(url, params=params).json()
    return JsonResponse(response.get('result'))

def save_deposit_products(request):
    url = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(url, params=params).json().get('result')

    for li in response.get('baseList'):
        serializer = DepositProductsSerializer(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('optionList'):
        serializer = DepositOptionsSerializer(data=li)
        product = DepositProducts.objects.get(fin_prdt_cd=li.get('fin_prdt_cd'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return JsonResponse({ "message": "save okay!" })

def deposit_products(request):
    pass

def deposit_product_options(request):
    pass

def top_rate(request):
    pass