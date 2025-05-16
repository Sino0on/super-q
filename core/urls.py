from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap  # new
from django.contrib.sitemaps.views import sitemap  # new

from main.models import Product

info_dict = {
    "queryset": Product.objects.all(),
    "date_field": "created_at",
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"products": GenericSitemap(info_dict)}},
        name="django.contrib.sitemaps.views.sitemap",
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
