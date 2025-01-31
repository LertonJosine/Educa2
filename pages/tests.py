from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView, TrainersPageView


class TestHomePage(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
    
    def test_home_page_use_right_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)



class AboutPagesTest(TestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
    
    
    def test_about_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_about_page_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_about_page_contain(self):
        self.assertContains(self.response, 'About')
    
    def test_about_page_uses_correct_view(self):
        view = resolve(reverse('about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


class TrainersPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('trainers')
        self.response = self.client.get(url)
    
    def test_about_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_about_page_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'trainers.html')
        self.assertContains(self.response, 'Trainers')
    
    def test_about_page_uses_correct_view(self):
        view = resolve(reverse('trainers'))
        self.assertEqual(view.func.__name__, TrainersPageView.as_view().__name__)
    