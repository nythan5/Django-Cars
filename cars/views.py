from django.shortcuts import render
from .models import Car


# Create your views here.


def teste(request):
    # usando 2 __ conseguimos acessar o atributo da tabela brand
    cars = Car.objects.filter(brand__name='Fiat')
    return render(
        request,
        template_name='cars.html',
        context={'cars': cars}
    )
