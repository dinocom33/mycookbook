from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio')
    list_filter = ('user',)
    search_fields = ('user',)
    fieldsets = (
        (
            'User',
            {
                'fields': (
                    'user',
                )
            }),
        (
            'First and Last names',
            {
                'fields': (
                    'first_name',
                    'last_name',
                )
            }),
        (
            'Avatar',
            {
                'fields': (
                    'avatar',
                )
            }),
        (
            'Additional information',
            {
                'fields': (
                    'bio',
                )
            }),
    )
