from django.shortcuts import render
from .models import TeamMember

def teams_page(request):
    team_members = TeamMember.objects.all()
    roles = {
        'President': team_members.filter(role='President'),
        'Head Officer': team_members.filter(role='Head Officer'),
        'Manager': team_members.filter(role='Manager'),
        'Supervisor': team_members.filter(role='Supervisor'),
        'Lead Engineer': team_members.filter(role='Lead Engineer'),
    }
    return render(request, 'teams/teams_page.html', {'roles': roles})