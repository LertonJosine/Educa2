from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = get_user_model()
    form_class = CustomUserCreationForm


class Profile(UpdateView):
    template_name = 'registration/profile.html'
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')