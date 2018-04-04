from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import (Badge, Bet, HistoricBankroll, Leg, ProfileBadge,
  Profile, Game, Season, Team, Week)

admin.site.register(Profile)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(Week)
admin.site.register(Game)
admin.site.register(Bet)
admin.site.register(Leg)
admin.site.register(HistoricBankroll)
admin.site.register(Badge)
admin.site.register(ProfileBadge)







