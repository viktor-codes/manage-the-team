from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Team
from .serializers import EmployeeSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
