from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = get_user_model()
    form_class = CustomUserCreationForm


class Profile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'registration/profile.html'
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    
    def test_func(self):
        user = self.request.user
        return user == self.get_object()