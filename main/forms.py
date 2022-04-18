from django.forms import ModelForm
from .models import Abc


class CreateAbcForm(ModelForm):
    class Meta:
        model = Abc
        fields = ['task', 'a', 'b', 'c']
