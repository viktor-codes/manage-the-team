from django.contrib import admin
from .models import Employee, Team


class TeamInline(admin.TabularInline):
    model = Employee.teams.through


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "user_email",
        "first_name",
        "last_name",
        "is_active",
        "date_joined",
    )
    list_filter = ("is_active", "teams", "date_joined")
    search_fields = (
        "first_name",
        "last_name",
        "user__email",
    )
    ordering = ("date_joined",)
    inlines = [TeamInline]

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = "Email"

    exclude = ("teams",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    inlines = [TeamInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super(TeamAdmin, self).get_inline_instances(request, obj)
