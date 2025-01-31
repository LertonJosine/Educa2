from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course


class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TrainersPageView(TemplateView):
    template_name = 'trainers.html'