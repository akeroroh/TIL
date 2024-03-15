from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('send/', views.send, name="send"),
    path('receive/', views.receive, name="receive"),
]
