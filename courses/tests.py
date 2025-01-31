from django.test import TestCase
from django.urls import resolve, reverse
from .models import Course
from django.contrib.auth import get_user_model
from .views import ListCoursesView, CourseDetailsPageView


class ListCoursesPageTest(TestCase):
    def setUp(self):    
        url = reverse('list-courses')
        self.response = self.client.get(url)
    
    def test_list_courses_page_name(self):
        self.assertEqual(self.response.status_code, 200)  
    
    def test_list_courses_template(self):
        self.assertTemplateUsed(self.response, 'list_courses.html')
        self.assertContains(self.response, 'Courses')
    
    def test_list_courses_view_used(self):
        view = resolve(reverse('list-courses'))
        self.assertEqual(view.func.__name__, ListCoursesView.as_view().__name__)


class CourseDetailsPageTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com'
        )
        course = Course.objects.create(
            trainer=user,
            name='test course',
            resume='this is a course for testing purpouses',
            cover='./media/course-1.jpg',
            sits=10,
            price=0.00,
        )
        url = reverse('course-detail', args=str(course.pk))
        
        self.response = self.client.get(url)
        
    def test_course_details_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_course_details_template(self):
        self.assertTemplateUsed(self.response, 'course-detail.html')
        self.assertContains(self.response, 'Course Details')
    
    def test_course_details_view_used(self):
        view = resolve(reverse('course-detail', args='1'))
        self.assertEqual(view.func.__name__, CourseDetailsPageView.as_view().__name__)

    
    
class CourseCreationTest(TestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(username='test', email='test@gmail.com', password='test123')        
        self.course = Course.objects.create(
            trainer=self.superuser,
            name='test course',
            resume='test course creation',
            cover='./media/course-1.jpg',
            price=20.00,
            sits=10         
            
        )
                    
    def test_course_creation(self):
        self.assertEqual(self.course.trainer, self.superuser)
        self.assertEqual(self.course.name, 'test course')
        self.assertEqual(self.course.resume, 'test course creation')
        self.assertEqual(self.course.price, 20.00)
        self.assertEqual(self.course.sits, 10)