import json
import time
import urllib.request

import requests

from dashboard.models import League, LeagueManager

def update_league(leagues):
    for l in leagues:
        lea = League()
        lea.league_id = int(l['league']['id'])
        lea.league_name = l['league']['name']
        lea.standings = l['standings']
        lea.save()

def update_managers(league_id, managers):
    for m in managers:
        man = LeagueManager()
        man.league_id = m[league_id]
        man.manager_id = m['id']
        man.manager_name = m['player_name']
        man.manager_team_name = m['entry_name']
        man.save()
