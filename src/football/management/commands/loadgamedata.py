from django.core.management.base import BaseCommand, CommandError
from football.models import Game, Week, Team
from datetime import datetime, timedelta
import arrow
import json

NFL_SCHEDULE = {
  arrow.get(2017, 9, 6).datetime: 's2017.w1',
  arrow.get(2017, 9, 13).datetime: 's2017.w2',
  arrow.get(2017, 9, 20).datetime: 's2017.w3',
  arrow.get(2017, 9, 27).datetime: 's2017.w4',
  arrow.get(2017, 10, 4).datetime: 's2017.w5',
  arrow.get(2017, 10, 11).datetime: 's2017.w6',
  arrow.get(2017, 10, 18).datetime: 's2017.w7',
  arrow.get(2017, 10, 25).datetime: 's2017.w8',
  arrow.get(2017, 11, 1).datetime: 's2017.w9',
  arrow.get(2017, 11, 8).datetime: 's2017.w10',
  arrow.get(2017, 11, 15).datetime: 's2017.w11',
  arrow.get(2017, 11, 22).datetime: 's2017.w12',
  arrow.get(2017, 11, 29).datetime: 's2017.w13',
  arrow.get(2017, 12, 6).datetime: 's2017.w14',
  arrow.get(2017, 12, 13).datetime: 's2017.w15',
  arrow.get(2017, 12, 20).datetime: 's2017.w16',
  arrow.get(2017, 12, 27).datetime: 's2017.w17',
}

def lookup_week(schedule_dict, lookup_date):
    ONE_WEEK = timedelta(days=7)
    for start, week_id in schedule_dict.items():
        if start <= lookup_date <= start + ONE_WEEK:
            return week_id

class Command(BaseCommand):
  help = "Reads in game data from <file>.  Expects data in a list of JSON: \n[{gametime, away, home, away_score, home_score, away_spread, home_spread, over_under, away_ml, home_ml}, ...]"

  def add_arguments(self, parser):
    parser.add_argument('file', help='JSON file to import', nargs=1)

  def handle(self, *args, **options):
    filename = options['file'][0]
    ONE_DAY = timedelta(days=1)

    with open(filename) as json_data:
      game_data = json.load(json_data)
      
    for g in game_data:
      print(g)

      # Get the appropriate week object or default
      g['game_time'] = arrow.get(g['game_time']).datetime
      week = lookup_week(NFL_SCHEDULE, g['game_time'])
      if (week):
        week_obj = Week.objects.get(week_id=week)
      else:
        week_obj = Week.objects.get(week_id='DEFAULT')
      g['week'] = week_obj

      # get the home and away instance objects as well
      g['away'] = Team.objects.get(abbr=g['away'])
      g['home'] = Team.objects.get(abbr=g['home'])

      # Calculate a date range for our game query
      start = g['game_time'] - ONE_DAY
      end = g['game_time'] + ONE_DAY

      print(g)

      try:
        obj = Game.objects.get(home=g['home'], away=g['away'], game_time__gt=start, game_time__lt=end)
        for key, value in g.items():
          setattr(obj, key, value)
        obj.save()
        self.stdout.write(self.style.SUCCESS('Updated....'))

      except Game.DoesNotExist:
        obj = Game(**g)
        print(obj)
        obj.save()
        self.stdout.write(self.style.SUCCESS('Created ....'))

    self.stdout.write(self.style.SUCCESS('Successfully processed "%s"' % filename))

  