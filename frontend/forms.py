from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2',)
