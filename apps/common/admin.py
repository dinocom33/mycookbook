from django.contrib import admin

from apps.common.models import CommentsModel, Contact


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'published_date', 'recipe', 'user')
    list_filter = ('published_date', 'recipe', 'user')
    search_fields = ('text', 'recipe', 'user')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'subject', 'message', 'date_sent')
    list_filter = ('email', 'first_name', 'last_name', 'subject', 'date_sent')
    search_fields = ('email', 'first_name', 'last_name', 'subject', 'date_sent')
    readonly_fields = ('date_sent',)
