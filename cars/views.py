from django.shortcuts import render
from .models import Car


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
