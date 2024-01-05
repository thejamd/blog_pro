from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import signupForm
# Create your views here.
class UserRegister(generic.CreateView):
    form_class = signupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
class UserEdit(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user