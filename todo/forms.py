from django import forms
from django.forms import ModelForm
from .models import *

class EditTodoItem(forms.ModelForm):
    class  Meta:
        model = Todo
        fields = '__all__'