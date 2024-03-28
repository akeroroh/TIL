from django.urls import path
from . import views


app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:restaurant_pk>', views.detail, name='detail'),
    path('<int:restaurant_pk>/edit/', views.edit_restaurant, name='edit_restaurant'),
    path('<int:restaurant_pk>/update/', views.update_restaurant, name='update_restaurant'),
    path('<int:restaurant_pk>/delete/', views.delete, name="delete"),
]   