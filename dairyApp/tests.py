import email
from django.test import TestCase
from dairyApp.models import User
import environ
import os
from pathlib import Path
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, '.env'))

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email=env('email1'), password='abcedfg123')
        User.objects.create(email=env('email2'), password='abcedfg123')
        User.objects.create(email=env('email3'), password='abcedfg123')
        
    
    def test_is_user(self):
        user1 = User.objects.get(email=env('email1'))
        user2 = User.objects.get(email=env('email2'))
        user3 = User.objects.get(email=env('email3'))
        self.assertEqual(user1.email, env('email1'))
        self.assertEqual(user2.email, env('email2'))
        self.assertEqual(user3.email, env('email3'))

        # try:
        #     User.objects.create(email=env('email1'), password='gwowjgoajgowjg123')
        # except Exception:
        #     self.assertEqual(True, True)

        count_users = User.objects.all().count()
        self.assertEqual(count_users, 3)

