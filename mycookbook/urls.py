from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'My cookbook Administration'
admin.site.site_title = 'My cookbook Administration'
admin.site.index_title = 'My cookbook App'

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', include('apps.common.urls')),
                  path('profile/', include('apps.user_profile.urls')),
                  path('recipes/', include('apps.recipes.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    handler400 = 'apps.common.views.bad_request'
    handler403 = 'apps.common.views.permission_denied'
    handler500 = 'apps.common.views.server_error'
