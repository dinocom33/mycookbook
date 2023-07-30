from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.common.forms import LoginForm


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@localhost.com', password='testpassword')

    def test_login_view_accessible_when_not_logged_in(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/login.html')

    def test_login_view_redirects_to_index_when_logged_in(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('index'))

    def test_login_view_with_valid_credentials(self):
        # Simulate a POST request to the view with valid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })

        # Check that the response redirects to the correct URL
        expected_url = reverse('edit profile', args=[self.user.pk])
        self.assertRedirects(response, expected_url)

    def test_login_view_with_invalid_credentials(self):
        # Simulate a POST request to the view with invalid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })

        # Check that the user is not logged in and stays on the login page
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/login.html')

    def test_login_view_remember_me(self):
        # Simulate a POST request to the view with "remember me" checked
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
            'remember_me': True,
        })

        # Check that the session expiration is set accordingly
        self.assertFalse(self.client.session.get_expire_at_browser_close())

    def test_login_view_no_remember_me(self):
        # Simulate a POST request to the view with "remember me" unchecked
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
            'remember_me': False,
        })

        # Check that the session expiration is set accordingly
        self.assertTrue(self.client.session.get_expire_at_browser_close())
