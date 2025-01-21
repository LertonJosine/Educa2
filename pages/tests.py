from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class TestHomePage(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
        self.assertContains(self.response, 'Novo conteudo')
    
    def test_home_page_use_right_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
