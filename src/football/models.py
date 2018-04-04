from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RestaurantLocation(models.Model):
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True)

class Season(models.Model):
    season_id       = models.CharField(max_length=50, primary_key=True)
    league          = models.CharField(max_length=120)
    year            = models.IntegerField()
    name            = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Week(models.Model):
    week_id         = models.CharField(max_length=50, primary_key=True)
    season          = models.ForeignKey('Season', on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    week_number     = models.DecimalField(max_digits=2, decimal_places=0)
    betting_open    = models.DateTimeField()
    betting_close   = models.DateTimeField()
    def __str__(self):
        return self.week_id

class Profile(models.Model):
    username        = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE, related_name='+', primary_key=True)
    bankroll        = models.IntegerField()
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.username}'    

class HistoricBankroll(models.Model):
    profile           = models.ForeignKey('Profile', on_delete=models.CASCADE)
    week              = models.ForeignKey('Week', on_delete=models.CASCADE)
    starting_bankroll = models.DecimalField(max_digits=100, decimal_places=0)

    def __str__(self):
        return f'{self.profile} {self.week}'
    
    def natural_key(self):
        return (self.profile, self.week)
    
    class Meta:
        unique_together = (('profile', 'week'),)

class Badge(models.Model):
    name            = models.CharField(max_length=50, unique=True)
    description     = models.CharField(max_length=200)
    img_file        = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)

class ProfileBadge(models.Model):
    profile         = models.ForeignKey('Profile', on_delete=models.CASCADE)
    badge           = models.ForeignKey('Badge', on_delete=models.CASCADE)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile} {self.badge}'

    class Meta:
        unique_together = (('profile', 'badge'),)

class Team(models.Model):
    abbr            = models.CharField(max_length=3, primary_key=True)
    city            = models.CharField(max_length=100)
    name            = models.CharField(max_length=100)

    def __str__(self):
        return self.abbr

class Game(models.Model):
    week            = models.ForeignKey('Week', on_delete=models.CASCADE)
    away            = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_team')
    home            = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_team')
    game_time       = models.DateTimeField(null=True, blank=True)
    network         = models.CharField(max_length=50, blank=True)
    money_line_home = models.CharField(max_length=10, blank=True)
    money_line_away = models.CharField(max_length=10, blank=True)
    spread_home     = models.CharField(max_length=10, blank=True)
    over_under      = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    away_final      = models.IntegerField(null=True, blank=True)
    home_final      = models.IntegerField(null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.week} {self.away}@{self.home}'

    class Meta:
        verbose_name_plural = 'Schedule'


class Bet(models.Model):
    profile         = models.ForeignKey('Profile', on_delete=models.CASCADE)
    amount          = models.IntegerField()
    odds            = models.CharField(max_length=50, blank=True)
    BET_TYPES = (
        ('Moneyline', 'Moneyline'),
        ('Spread', 'Spread'),  
        ('Over', 'Over'), 
        ('Under', 'Under'),
        ('Parlay', 'Parlay'),
        ('Tease', 'Tease'),
        ('Interest', 'Interest')
    )
    type            = models.CharField(max_length=50, choices=BET_TYPES, null=True, blank=True)
    BET_RESULTS = (
        (None, ''),
        ('Win', 'Win'),
        ('Lose', 'Lose'),
        ('Push', 'Push'),
    )
    result          = models.CharField(max_length=50, choices=BET_RESULTS, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile} {self.amount} {self.type}'


class Leg(models.Model):
    bet             = models.ForeignKey('Bet', on_delete=models.CASCADE)
    game            = models.ForeignKey('Game', on_delete=models.CASCADE)
    LEG_TYPES = (
        ('Moneyline', 'Moneyline'),
        ('Spread', 'Spread'),  
        ('Over', 'Over'), 
        ('Under', 'Under'),
    )
    type            = models.CharField(max_length=50, choices=LEG_TYPES)
    leg             = models.CharField(max_length=50)
    odds            = models.CharField(max_length=50)
    LEG_RESULTS = (
        (None, ''),
        ('Win', 'Win'),
        ('Lose', 'Lose'),
        ('Push', 'Push'),
    )
    result          = models.CharField(max_length=50, choices=LEG_RESULTS, null=True, blank=True)

    def __str__(self):
        return f'{self.game} {self.type} {self.odds}'

    def natural_key(self):
        return (self.bet, self.game, self.type)

    class Meta:
        unique_together = (('bet', 'game', 'type'),)
