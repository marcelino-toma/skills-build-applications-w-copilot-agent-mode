from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')
    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team, is_superhero=True)
        self.assertEqual(str(user), 'batman')
    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(email='ironman@marvel.com', username='ironman', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2024-01-01')
        self.assertEqual(str(activity), 'ironman - run (2024-01-01)')
    def test_workout_creation(self):
        user = User.objects.create(email='spiderman@marvel.com', username='spiderman', is_superhero=True)
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        workout.suggested_for.add(user)
        self.assertEqual(str(workout), 'Pushups')
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Marvel - 100 pts')
