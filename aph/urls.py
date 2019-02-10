from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('fake-data/', include('fake_data_gen.urls')),
    path('accounts/', include('accounts.urls')),
    path('reset/', include('accounts.url_reset')),
    path('listings/', include('listings.urls')),
    path('enquiries/', include('enquiries.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
