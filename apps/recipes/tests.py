from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.recipes.models import Recipe


class CreateRecipeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_recipe_view(self):
        self.client.login(username='testuser', password='testpassword')

        # Simulate a POST request to the view
        response = self.client.post(reverse('add recipe'), {
            'title': 'Test Recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1, Step 2',
            'category': 'Dessert',
            'image_url': 'https://example.com/image.jpg'
        })

        # Check that the response has a successful status code
        self.assertEqual(response.status_code, 302)

        # Check that the recipe was created and assigned to the logged-in user
        recipe = Recipe.objects.get(title='Test Recipe')
        self.assertEqual(recipe.created_by, self.user)

        # Check the redirect URL
        expected_url = reverse('my recipes', kwargs={'pk': self.user.pk})
        self.assertRedirects(response, expected_url)
