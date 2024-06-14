from django.shortcuts import render, redirect
from .models import Car
from .forms import *


# Create your views here.


def car_list(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')

    return render(
        request,
        template_name='cars.html',
        context={'cars': cars}
    )


def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car:list')

    else:
        form = CarForm()
    return render(request, template_name='create.html', context={'form': form})
