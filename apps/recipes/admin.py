from django.contrib import admin

from apps.common.models import CommentsModel
from apps.recipes.models import Recipe, FavoriteRecipeModel, LikedRecipe, Rating


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at', 'likes_count', 'favorite_count', 'comments_count')
    list_filter = ('created_by', 'created_at', 'updated_at', 'title')
    search_fields = ('created_by', 'created_at', 'updated_at', 'title')
    auto_populate_field = ('slug',)
    readonly_fields = ('created_at', 'updated_at', 'slug')
    fieldsets = (
        (
            'Title',
            {
                'fields': (
                    'title',
                )
            }),
        (
            'Ingredients',
            {
                'fields': (
                    'ingredients',
                )
            }),
        (
            'Instructions',
            {
                'fields': (
                    'instructions',
                )
            }),
        (
            'Category',
            {
                'fields': (
                    'category',
                )
            }),
        (
            'Image',
            {
                'fields': (
                    'image_url',
                )
            }),
        (
            'Created and updated dates',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }),
        (
            'Slug',
            {
                'fields': (
                    'slug',
                )
            }),

    )

    def likes_count(self, obj):
        return LikedRecipe.objects.filter(recipe=obj).count()

    likes_count.short_description = 'Likes'

    def favorite_count(self, obj):
        return FavoriteRecipeModel.objects.filter(recipe=obj).count()

    favorite_count.short_description = 'Favorite to'

    def comments_count(self, obj):
        return CommentsModel.objects.filter(recipe=obj).count()

    comments_count.short_description = 'Comments'


@admin.register(FavoriteRecipeModel)
class AdminFavoriteRecipe(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')

    fieldsets = (
        (
            'User',
            {
                'fields': (
                    'user',
                )
            }),
        (
            'Liked Recipe',
            {
                'fields': (
                    'recipe',
                )
            }
        )
    )


@admin.register(LikedRecipe)
class AdminLikedRecipe(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'liked_date')
    list_filter = ('user', 'recipe', 'liked_date')
    search_fields = ('user', 'recipe', 'liked_date')
    readonly_fields = ('liked_date',)

    fieldsets = (
        (
            'User',
            {
                'fields': (
                    'user',
                )
            }),
        (
            'Liked Recipe',
            {
                'fields': (
                    'recipe',
                )
            }),
        (
            'Liked Date',
            {
                'fields': (
                    'liked_date',
                )
            }),
    )


@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'rating')
    list_filter = ('user', 'recipe', 'rating')
    search_fields = ('user', 'recipe', 'rating')
    fieldsets = (
        (
            'User',
            {
                'fields': (
                    'user',
                )
            }),
        (
            'Recipe',
            {
                'fields': (
                    'recipe',
                )
            }),
        (
            'Rating',
            {
                'fields': (
                    'rating',
                )
            }
        )
    )
