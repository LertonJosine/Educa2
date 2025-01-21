from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from .forms import CustomUserCreationForm
from .views import SignUpView


class ModeloUsuario(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123#'
            )
        
        self.super_user = get_user_model().objects.create_superuser(
            username='superuser',
            email='superuser@gmail.com',
            password='superuser123#'
        )
        
    def test_user_creation(self):       
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertEqual(self.user.is_superuser, False)
    
    def test_superuser_creation(self):        
        self.assertEqual(self.super_user.username, 'superuser')
        self.assertEqual(self.super_user.email, 'superuser@gmail.com')
        self.assertEqual(self.super_user.is_superuser, True)

        
class SignupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    
    def test_signup_page_url(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_sigup_page_template(self):
        self.assertContains(self.response, 'Signup')
        self.assertTemplateUsed(self.response, 'registration/signup.html')
    
    def test_signup_form_used(self):
        form = self.response.context['form']
        self.assertIsInstance(form, CustomUserCreationForm)
    
    def test_signup_page_use_correct_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
        