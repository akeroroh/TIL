from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/update/', views.staff_update, name="staff_update"),
    path('delete/', views.delete, name="delete"),
]