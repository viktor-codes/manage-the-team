from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, TeamViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"teams", TeamViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
