from django.contrib.auth.models import User
from django.test import TestCase

from apps.common.models import CommentsModel
from apps.recipes.models import Recipe


class CommentsModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='testuser@localhost.com', password='testpassword')

        # Create a test recipe
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            ingredients='Ingredient 1, Ingredient 2',
            instructions='Step 1, Step 2',
            category='Dessert',
            image='https://example.com/image.jpg',
            created_by=self.user,
        )

    def test_comments_model_creation(self):
        # Create a comment for the recipe
        comment = CommentsModel.objects.create(
            text='This is a test comment.',
            recipe=self.recipe,
            user=self.user,
        )

        # Check that the comment is created successfully
        self.assertEqual(comment.text, 'This is a test comment.')
        self.assertEqual(comment.recipe, self.recipe)
        self.assertEqual(comment.user, self.user)

    def test_comments_model_str_representation(self):
        # Create a comment for the recipe
        comment = CommentsModel.objects.create(
            text='Another test comment.',
            recipe=self.recipe,
            user=self.user,
        )

        # Check that the str representation is as expected
        self.assertEqual(str(comment), f'{self.user} - {self.recipe.title}')

    def test_comments_model_ordering(self):
        # Create two comments with different published dates
        comment1 = CommentsModel.objects.create(
            text='Comment 1',
            recipe=self.recipe,
            user=self.user,
        )

        comment2 = CommentsModel.objects.create(
            text='Comment 2',
            recipe=self.recipe,
            user=self.user,
        )

        # Check that the ordering is based on the published_date in descending order
        comments = CommentsModel.objects.all()
        self.assertEqual(list(comments), [comment2, comment1])
