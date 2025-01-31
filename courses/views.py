from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course


class ListCoursesView(ListView):
    model = Course
    template_name = 'list_courses.html'
    context_object_name = 'courses'
    permission_required = ('special_status')


class CourseDetailsPageView(DetailView):
    model = Course
    template_name = 'course-detail.html'
    context_object_name = 'course'
    
