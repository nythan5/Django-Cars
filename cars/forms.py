from django import forms
from cars.models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
