from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('deposit-products/', views.deposit_products, name="deposit_products"),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name="deposit_product_optins"),
    path('deposit-products/top_rate/', views.top_rate, name="top_rate"),
]