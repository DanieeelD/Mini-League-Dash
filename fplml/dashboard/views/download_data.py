from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from dashboard.forms import LeagueForm
from dashboard.models import League, LeagueManager, ManagerGWHistory
from dashboard.views.getters import get_league_data, get_manager_ids, get_manager_information, get_manager_history, get_manager_team_per_week
from dashboard.views.updates import update_league, update_managers

def DownloadLeagueView(request):
    try:
        page = 1
        leagues = get_league_data('league_id', page)
        update_league(leagues)
    except Exception as e:
        messages.error(request, f"Failure downloading your league")

        return redirect("dashboard/dashboard.html")