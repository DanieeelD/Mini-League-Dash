from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
import requests
import json

def get_league_data(league_id: int, page):
    url = "https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings?page_standings={page}"
    response = requests.get(url)
    responseStr = response.text
    data = json.loads(responseStr)
    return data

def get_manager_ids(league_id):
    page = 1
    manager_ids = get_league_data(league_id, page)['standings']
    managers = defaultdict(list)
    if manager_ids['has_next'] == "false":
        for m in manager_ids['results']:
            managers[1].append(m)
            return managers
    while manager_ids['has_next'] == "true":
        for m in manager_ids['results']:
            managers[1].append(m)
            page += 1 
            manager_ids = get_league_data(league_id, page)
    else:
        managers[1].append(m)
        return managers

def get_manager_information(manager_id):
    url = "https://fantasy.premierleague.com/api/entry/{manager_id}/"
    response = requests.get(url)
    responseStr = response.text
    data = json.loads(responseStr)
    return data

def get_manager_history(manager_id):
    url = "https://fantasy.premierleague.com/api/entry/{manager_id}/history"
    response = requests.get(url)
    responseStr = response.text
    data = json.loads(responseStr)
    return data

def get_manager_team_per_week(manager_id):
    event_num = 1
    manager_team = {}
    while event_num != 39:
        url = "https://fantasy.premierleague.com/api/entry/{manager_id}/event/{event_num}/picks/"
        response = requests.get(url)
        responseStr = response.text
        data = json.loads(responseStr)
        manager_team |= data # |= appends data returned from manager team API (dict) to another dictionary through merging
        event_num += 1
    return manager_team
    
