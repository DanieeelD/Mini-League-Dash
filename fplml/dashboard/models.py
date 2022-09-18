from django.db import models

# Create your models here.

class League(models.Model):
    league_id = models.IntegerField(unique="True")
    league_name = models.CharField(max_length=200)
    standings = models.JSONField(null="FALSE")

    def __str__(self):
        return self.league_name

class LeagueManager(models.Model):
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    manager_id = models.IntegerField(null="FALSE")
    manager_name = models.CharField(max_length=200)
    manager_team_name = models.CharField(max_length=201)

    '''
    class Meta:
        unique_together = ('league_id', 'manager_id')
    '''

    def __str__(self):
        return self.manager_id

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['league_id','manager_id'], name='unique_league_manager')
        ]


class ManagerGWHistory(models.Model):
    manager_id = models.ForeignKey(LeagueManager, on_delete=models.CASCADE)
    event_id = models.IntegerField(null="FALSE")
    gw_points = models.IntegerField()
    overall_rank = models.IntegerField()
    gw_team_value = models.IntegerField()
    gw_points_on_bench = models.IntegerField()
    event_transfers = models.IntegerField()
    event_transfers_cost = models.IntegerField()
    automatic_subs = models.JSONField()
    active_chip = models.CharField(max_length=200)
    gw_captain_id = models.IntegerField()
    gw_vice_captain_id = models.IntegerField()
