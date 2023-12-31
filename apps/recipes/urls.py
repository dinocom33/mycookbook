from django.urls import path

from .views import CreateRecipeView, MyRecipesView, RecipesDetailsView, AllRecipeListView, MyRecipesDetailsView, \
    SearchResultsView, RecipeByCategoryView, EditRecipeView, RecipeDeleteView, AddRemoveFavoritesView, FavoriteListView, \
    hit_like_button, rate_recipe_view, RecipeByCuisineView

urlpatterns = [
    path('all-recipes/', AllRecipeListView.as_view(), name='all recipes'),
    path('search/', SearchResultsView.as_view(), name='search results'),
    path('add-recipe/', CreateRecipeView.as_view(), name='add recipe'),
    path('my-recipes/<int:pk>/', MyRecipesView.as_view(), name='my recipes'),
    path('my-recipe-details/<int:pk>/<slug:slug>/', MyRecipesDetailsView.as_view(),
         name='my recipe details'),
    path('my-favorites/add/<int:pk>/<slug:slug>/', AddRemoveFavoritesView.as_view(), name='add to favorites'),
    path('rate/<int:pk>/<slug:slug>/', rate_recipe_view, name='rate recipe'),
    path('my-favorites/<int:pk>/', FavoriteListView.as_view(), name='favorite recipes'),
    path('category/<str:category>/', RecipeByCategoryView.as_view(), name='recipe by category'),
    path('cuisine/<str:cuisine>/', RecipeByCuisineView.as_view(), name='recipe by cuisine'),
    path('details/<int:pk>/<slug:slug>/', RecipesDetailsView.as_view(), name='recipe details'),
    path('edit/<int:pk>/<slug:slug>/', EditRecipeView.as_view(), name='edit recipe'),
    path('delete/<int:pk>/<slug:slug>/', RecipeDeleteView.as_view(), name='delete recipe'),
    path('details/<int:pk>/<slug:slug>/like/', hit_like_button, name='like recipe'),
]
