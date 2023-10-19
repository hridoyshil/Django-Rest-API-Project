from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from firstapp.views import homeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView),
    path("api/", include("rest_framework.urls")),
    path("api/firstapp/", include("firstapp.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
