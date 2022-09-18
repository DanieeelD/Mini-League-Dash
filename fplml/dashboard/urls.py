from django.urls import URLPattern
from django.urls import path
from dashboard.views.display_data import SearchLeagueView, DashboardView

urlpatterns = [
    path('', SearchLeagueView),
    ##path('dashboard/', DashboardView)
]