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
    response = requests.get(url, params=params).json()
    response2 = response.get('result')

    # for li in response2.get('baseList'):
    #     fin_prdt_cd = li.get('fin_prdt_cd')
    #     existing_product = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)
    #     if existing_product:
    #         continue
    #     kor_co_nm = li.get('kor_co_nm')
    #     fin_prdt_nm = li.get('fin_prdt_nm')
    #     etc_note = li.get('etc_note')
    #     join_deny = li.get('join_deny')
    #     join_member = li.get('join_member')
    #     join_way = li.get('join_way')
    #     spcl_cnd = li.get('spcl_cnd')

    #     save_data = {
    #         'fin_prdt_cd': fin_prdt_cd,
    #         'kor_co_nm': kor_co_nm,
    #         'fin_prdt_nm': fin_prdt_nm,
    #         'etc_note': etc_note,
    #         'join_deny': join_deny,
    #         'join_member': join_member,
    #         'join_way': join_way,
    #         'spcl_cnd': spcl_cnd,
    #     }

    #     serializer = DepositProductsSerializer(data=save_data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()

    for li in response2.get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')

        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        print(product)
        save_data = {
            'product': product,
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }

        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({ "message": "save okay!" })

def deposit_products(request):
    pass

def deposit_product_options(request):
    pass

def top_rate(request):
    pass