from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", views.home, name="home"),
    path("teams/", views.teams_page, name="teams"),
    path("teams/<int:team_id>/", views.team_detail, name="team_detail"),
]
