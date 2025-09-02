from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
        User.objects.create(email='cap@marvel.com', name='Captain America', team='marvel', is_superhero=True)
        User.objects.create(email='thor@marvel.com', name='Thor', team='marvel', is_superhero=True)
        User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_superhero=True)
        User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True)

        # Activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2025-09-01')
        Activity.objects.create(user='Captain America', type='cycle', duration=45, date='2025-09-01')
        Activity.objects.create(user='Thor', type='swim', duration=60, date='2025-09-01')
        Activity.objects.create(user='Superman', type='fly', duration=120, date='2025-09-01')
        Activity.objects.create(user='Batman', type='train', duration=90, date='2025-09-01')
        Activity.objects.create(user='Wonder Woman', type='run', duration=40, date='2025-09-01')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=135)
        Leaderboard.objects.create(team='dc', points=250)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Sprint for 100m', difficulty='medium')
        Workout.objects.create(name='Flying', description='Fly for 1 hour', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
