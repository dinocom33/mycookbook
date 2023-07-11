from django.contrib import admin

from apps.common.models import CommentsModel


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'published_date', 'recipe', 'user')
    list_filter = ('published_date', 'recipe', 'user')
    search_fields = ('text', 'recipe', 'user')


