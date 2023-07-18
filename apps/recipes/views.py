from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.views.generic.edit import FormMixin
from django.db.models import Q, Avg
from django.contrib import messages

from apps.common.forms import CommentForm
from apps.recipes.models import LikedRecipe, Rating
from apps.recipes.forms import AddToFavoriteForm
from apps.recipes.models import Recipe, FavoriteRecipeModel


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'category', 'image']
    template_name = 'recipes/create_recipe.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy('my recipes', kwargs={'pk': user_pk})


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe-confirm-delete.html'
    success_url = reverse_lazy('my recipes')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.created_by or self.request.user.is_staff

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy('my recipes', kwargs={'pk': user_pk})


class EditRecipeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'category', 'image']
    template_name = 'recipes/edit_recipe.html'

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.created_by or self.request.user.is_staff

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AllRecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/all-recipes.html'
    context_object_name = 'all_recipes'
    paginate_by = 6
    queryset = Recipe.objects.all().order_by('-created_at')


class RecipesDetailsView(FormMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={'pk': self.kwargs['pk'], 'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super(RecipesDetailsView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'recipe': self.object})
        if self.request.user.is_authenticated:
            context['liked_recipe'] = LikedRecipe.objects.filter(user=self.request.user, recipe=self.object).exists()
            context['added_to_favorite'] = FavoriteRecipeModel.objects.filter(
                user=self.request.user,
                recipe__pk=self.kwargs['pk']).exists()
            context['avg_rating'] = Rating.objects.filter(recipe=self.object).aggregate(Avg("rating"))["rating__avg"] or 0

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.recipe = Recipe.objects.filter(pk=self.kwargs['pk'], slug=self.kwargs['slug']).get()
        form.save()
        return super().form_valid(form)


class MyRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/my-recipes.html'
    context_object_name = 'my_recipes'
    paginate_by = 6
    queryset = Recipe.objects.none()

    def get_queryset(self):
        return Recipe.objects.filter(created_by=self.request.user).order_by('-created_at')


class MyRecipesDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/my-recipe-details.html'

    def get_success_url(self):
        return reverse('my recipe details', kwargs={'pk': self.kwargs['pk'], 'slug': self.kwargs['slug']})


class SearchResultsView(ListView):
    model = Recipe
    template_name = 'recipes/search-results.html'
    context_object_name = 'search_results'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(Q(title__icontains=query) |
                                         Q(ingredients__icontains=query)).order_by('-created_at')
        return Recipe.objects.all().order_by('-created_at')


class RecipeByCategoryView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-by-category.html'
    context_object_name = 'recipe_by_category'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context

    def get_queryset(self):
        category = self.kwargs['category']
        return Recipe.objects.filter(category=category).order_by('-created_at')


class AddToFavoritesView(LoginRequiredMixin, FormMixin, DetailView):
    model = Recipe
    form_class = AddToFavoriteForm
    template_name = 'recipes/recipe-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_favorite_form'] = AddToFavoriteForm()

        return context

    def post(self, request, *args, **kwargs):
        recipe_pk = self.kwargs['pk']
        user = request.user

        if not FavoriteRecipeModel.objects.filter(user=user, recipe__pk=recipe_pk).exists():
            recipe = Recipe.objects.get(pk=recipe_pk)
            favorite = FavoriteRecipeModel(user=user, recipe=recipe)
            favorite.save()
            messages.info(request, "This recipe was added to favorites.")

        return redirect('recipe details', pk=recipe_pk, slug=recipe.slug)


class RemoveFromFavoritesView(LoginRequiredMixin, FormMixin, DetailView):
    model = Recipe
    form_class = AddToFavoriteForm
    template_name = 'recipes/recipe-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['remove_from_favorite_form'] = AddToFavoriteForm()

        return context

    def post(self, request, *args, **kwargs):
        recipe_pk = self.kwargs['pk']
        user = request.user

        if FavoriteRecipeModel.objects.filter(user=user, recipe__pk=recipe_pk).exists():
            recipe = Recipe.objects.get(pk=recipe_pk)
            favorite = FavoriteRecipeModel.objects.get(user=user, recipe=recipe)
            favorite.delete()
            messages.info(request, "This recipe was removed from favorites.")

        return redirect('recipe details', pk=recipe_pk, slug=recipe.slug)


class FavoriteListView(LoginRequiredMixin, ListView):
    model = FavoriteRecipeModel
    template_name = 'recipes/favorite_list.html'
    context_object_name = 'favorites'
    paginate_by = 6

    def get_queryset(self):
        return self.request.user.favorite_recipes.all().order_by('-favoriterecipemodel__added_date')


@login_required
def hit_like_button(request, pk, slug):
    recipe = get_object_or_404(Recipe, pk=pk, slug=slug)
    user = request.user

    liked_recipe, created = LikedRecipe.objects.get_or_create(
        recipe=recipe,
        user=user
    )

    if not created:
        liked_recipe.delete()
        messages.info(request, "This recipe was disliked.")
    else:
        liked_recipe.save()
        messages.info(request, "This recipe was liked.")

    return redirect('recipe details', pk=recipe.pk, slug=recipe.slug)


@login_required
def rate_recipe_view(request, pk, slug):
    recipe = get_object_or_404(Recipe, pk=pk, slug=slug)
    rating = int(request.POST.get('rating', 0))

    if 0 < rating <= 5:
        recipe_rating, created = Rating.objects.get_or_create(user=request.user, recipe=recipe)

        if recipe_rating:
            recipe_rating.delete()

        recipe_rating.rating = rating
        recipe_rating.save()

    return redirect('recipe details', pk=recipe.pk, slug=recipe.slug)
