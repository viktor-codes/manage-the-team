from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("team_manager_api.urls")),
    path("", include("users.urls")),
]
