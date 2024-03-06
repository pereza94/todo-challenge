from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register("users", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("tasks/", include('tasks.urls')),

    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("swagger/schema/", SpectacularAPIView.as_view(), name="swagger-schema"),
    path("swagger/docs/", SpectacularSwaggerView.as_view(url_name="swagger-schema"), name="swagger-docs"),

]
