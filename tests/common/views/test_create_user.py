from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.common.forms import RegisterForm


class RegisterViewTest(TestCase):
    def test_register_view_accessible_when_not_logged_in(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/register.html')

    def test_register_view_redirects_to_index_when_logged_in(self):
        # Create a test user and log in
        User.objects.create_user(username='testuser', email='testuser@localhost.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('register user'))
        self.assertRedirects(response, reverse('index'))

    def test_register_view_creates_user(self):
        # Simulate a POST request to the view with valid form data
        response = self.client.post(reverse('register user'), {
            'username': 'newuser',
            'email': 'newuser@localhost.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })

        # Check that the response has a successful status code and user is created
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_view_invalid_form_submission(self):

        response = self.client.post(reverse('register user'), {
            'username': 'newuser',
            'email': 'newuser@localhost.com',
            'password1': 'newpassword123',
            'password2': 'differentpassword',
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_register_view_redirects_to_login_after_successful_registration(self):

        response = self.client.post(reverse('register user'), {
            'username': 'newuser',
            'email': 'newuser@localhost.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })

        self.assertRedirects(response, reverse('login'))
