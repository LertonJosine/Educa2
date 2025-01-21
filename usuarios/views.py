from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = get_user_model()
    form_class = CustomUserCreationForm
    