from django.urls import path
from .views import ListCoursesView, CourseDetailsPageView


urlpatterns = [
    path('list-courses/', ListCoursesView.as_view(), name='list-courses'),
    path('course-detail/<int:pk>/', CourseDetailsPageView.as_view(), name='course-detail'),
]
