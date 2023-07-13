from django import forms

from apps.recipes.models import Recipe, FavoriteRecipeModel, Rating


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class AddToFavoriteForm(forms.ModelForm):
    class Meta:
        model = FavoriteRecipeModel
        fields = '__all__'


class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
