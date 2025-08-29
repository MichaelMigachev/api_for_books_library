from django.contrib import admin
from django.urls import path, include


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("", include("library.urls", namespace="library")),
    # Документация
    # генерация OpenAPI-схемы
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    # Redoc UI
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
