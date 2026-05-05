from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel, is_superhero=True),
            User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel, is_superhero=True),
            User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel, is_superhero=True),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc, is_superhero=True),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc, is_superhero=True),
            User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc, is_superhero=True),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=users[3], type='swim', duration=60, date='2024-01-03')

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Yoga', description='Flexibility and balance')
        w1.suggested_for.add(users[0], users[1])
        w2.suggested_for.add(users[2], users[3])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Ensure unique index on email
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Database populated with test data and unique email index created.'))
