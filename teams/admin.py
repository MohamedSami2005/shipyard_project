from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'joined_at')
    search_fields = ('name', 'role')
    list_filter = ('role', 'joined_at')