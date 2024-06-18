from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Car
from .forms import *
from django.views.generic import ListView
from django.views import View


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


class CarCreateView(View):
    def get(self, request):
        form = CarForm()
        return render(request, template_name='create.html', context={'form': form})

    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car:list')
        return render(request, template_name='create.html', context={'form': form})
