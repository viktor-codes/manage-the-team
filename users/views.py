from django.shortcuts import render, get_object_or_404
from team_manager_api.models import Team, Employee


def home(request):
    return render(request, "users/home.html")


def teams_page(request):
    return render(request, "users/teams.html")


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    employees = Employee.objects.all()
    team_employees = team.employees.all()
    return render(
        request,
        "users/team_detail.html",
        {
            "team": team,
            "employees": employees,
            "team_employees": team_employees,
        },
    )
