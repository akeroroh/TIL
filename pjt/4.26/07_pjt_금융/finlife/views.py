from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import api_view
from .serializer import DepositOptionsSerializer, DepositProductsSerializer
from .models import DepositProducts, DepositOptions
from django.db.models import Max
import requests
from django.db import transaction
from rest_framework import status
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

@api_view(["GET", "POST"])
def deposit_products(request):
    if request.method == "GET":
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        product = DepositProductsSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_200_OK)

@api_view(["GET"])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositProducts.objects.velu(fin_prdt_cd-fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many = True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def top_rate(request):
    highest_rate = DepositOptions.objects.aggregate(('intr_rate2'))
    highest_rate_option = DepositOptions.objects.get(intr_rate2 = highest_rate.get('intr_rate2__max'))
    product_serializer = DepositProductsSerializer(highest_rate_option.product)
    option_serializer = DepositOptionsSerializer(highest_rate_option)
    return Response({'product': product_serializer.data, 'option' : option_serializer.data}, status=status.HTTP_200_OK)
