from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Car
from .forms import CarForm
from django.views.generic import ListView, CreateView, DetailView


# Create your views here.


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        qs = super().get_queryset().order_by('model')  # == Car.Objects.all().order_by('model') # noqa
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(model__icontains=search)
        return qs


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('car:list')


class CarDetailView(DetailView):
    model = Car
    template_name = 'detail.html'
    context_object_name = 'car'
