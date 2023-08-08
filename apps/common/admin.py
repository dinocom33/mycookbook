from django.contrib import admin

from apps.common.models import CommentsModel, Contact


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'published_date', 'recipe', 'user')
    list_filter = ('published_date', 'recipe', 'user')
    search_fields = ('text', 'recipe__title', 'user__username')
    readonly_fields = ('published_date',)
    fieldsets = (
        (
            'Comment',
            {
                'fields': (
                    'text',
                )
            }),
        (
            'Commented Recipe',
            {
                'fields': (
                    'recipe',
                )
            }),
        (
            'User',
            {
                'fields': (
                    'user',
                )
            }),
        (
            'Publication Date',
            {
                'fields': (
                    'published_date',
                )
            }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'subject', 'message', 'date_sent')
    list_filter = ('email', 'first_name', 'last_name', 'subject', 'date_sent')
    search_fields = ('email', 'first_name', 'last_name', 'subject', 'date_sent')
    readonly_fields = ('date_sent',)
    fieldsets = (
        (
            'Names',
            {
                'fields': (
                    'first_name',
                    'last_name',
                )
            }),
        (
            'Email',
            {
                'fields': (
                    'email',
                )
            }),
        (
            'Subject',
            {
                'fields': (
                    'subject',
                )
            }),
        (
            'Message',
            {
                'fields': (
                    'message',
                )
            }),
    )
