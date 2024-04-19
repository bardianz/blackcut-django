from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path('reserve/', include("reservation.urls")),
    path('api/', include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path("", include("home.urls"))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'بلک کات' 
admin.site.site_title = 'پنل مدیریت بلک کات'
admin.site.index_title=  'پنل مدیریت بلک کات'
