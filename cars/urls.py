from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.CarListView.as_view(), name='list'),
    path('new_car/', views.CarCreateView.as_view(), name='create'),
]
