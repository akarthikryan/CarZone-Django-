from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import TeamMember


def teams(request):
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members
    }
    return render(request, "teams/teams.html", context)
    
def team_member_detail(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)

    context = {
        "member": member
    }

    return render(request, "teams/teams_details.html", context)
    

