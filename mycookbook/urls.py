from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django_email_verification import urls as email_urls

admin.site.site_header = 'My cookbook Administration'
admin.site.site_title = 'My cookbook Administration'
admin.site.index_title = 'My cookbook App'

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', include('apps.common.urls')),
                  path('profile/', include('apps.user_profile.urls')),
                  path('recipes/', include('apps.recipes.urls')),
                  path('email/', include(email_urls), name='email-verification'),
              ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = TemplateView.as_view(template_name='404.html')
handler400 = TemplateView.as_view(template_name='404.html')
handler403 = TemplateView.as_view(template_name='404.html')
handler500 = TemplateView.as_view(template_name='500.html')
