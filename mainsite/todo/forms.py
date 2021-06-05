from django import forms
from django.forms import ModelForm 
from .models import Task #firstly import Task from models.py and then make form


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
