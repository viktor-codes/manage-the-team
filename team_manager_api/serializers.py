from rest_framework import serializers
from .models import Employee, Team


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "user",
            "email",
            "first_name",
            "last_name",
            "teams",
            "date_joined",
            "is_active",
        ]


class TeamSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "description", "employees", "created_at"]
