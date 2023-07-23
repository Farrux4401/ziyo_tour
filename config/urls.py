from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns, set_language
# from django.utils.translation import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("travel.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=True),
     # NEW
    path("<str:language>/", set_language, name="set-language"),
]
