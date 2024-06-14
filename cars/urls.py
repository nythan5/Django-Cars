from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.car_list, name='list'),
    path('new_car/', views.car_create, name='create'),
]
