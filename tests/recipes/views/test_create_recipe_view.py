from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from apps.recipes.models import Recipe


class CreateRecipeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='lZs9g@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_recipe_view_accessible(self):
        response = self.client.get(reverse('add recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/create-recipe.html')

    def test_create_recipe_view_with_valid_form_data(self):
        # Simulate a POST request to the view with valid form data
        response = self.client.post(reverse('add recipe'), {
            'title': 'Test Recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1, Step 2',
            'category': 'Dessert',
            'image': SimpleUploadedFile('test_image.jpg', b'Image content'),
        })

        # Check that the response redirects to the success URL
        user_pk = self.user.pk
        expected_url = reverse('my recipes', kwargs={'pk': user_pk})
        self.assertRedirects(response, expected_url)

        # Check that the recipe is created and assigned to the logged-in user
        recipe = Recipe.objects.get(title='Test Recipe')
        self.assertEqual(recipe.created_by, self.user)

    def test_create_recipe_view_with_invalid_form_data(self):
        # Simulate a POST request to the view with invalid form data
        response = self.client.post(reverse('add recipe'), {
            'title': '',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1, Step 2',
            'category': 'Dessert',
            'image': SimpleUploadedFile('test_image.jpg', b'Image content'),
        })

        # Check that the response status is 200 (form is not valid) and template used is 'recipes/create-recipe.html'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/create-recipe.html')

        # Check that the recipe is not created
        self.assertFalse(Recipe.objects.exists())

    def test_create_recipe_view_redirects_to_login_for_anonymous_user(self):
        # Log out the user
        self.client.logout()

        # Simulate a GET request to the view
        response = self.client.get(reverse('create_recipe'))

        # Check that the response redirects to the login page
        expected_url = reverse('login')
        self.assertRedirects(response, expected_url)
