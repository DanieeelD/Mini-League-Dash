from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from dashboard.forms import LeagueForm
from dashboard.views.download_data import DownloadLeagueView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
import requests

def SearchLeagueView(request):
    form = LeagueForm(request.GET)
    if form.is_valid():
        league_id = form.cleaned_data['league_id']
        DownloadLeagueView(request)
        return redirect(request, "dashboard/search_league.html")

    context = {
        "form":form
    }

    return render(request, "dashboard/search_league.html", context)

def DashboardView(request):
    return render(request, "dashboard/search_league.html")
