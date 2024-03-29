from django.urls import path
from . import views

app_name = 'memos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:memos_pk>', views.detail, name='detail'),
    path('<int:memos_pk>/delete/', views.delete, name='delete'),
]
