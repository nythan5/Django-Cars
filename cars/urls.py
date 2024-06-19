from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.CarListView.as_view(), name='list'),
    path('new_car/', views.CarCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.CarDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CarUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CarDeleteView.as_view(), name='delete'),

]
