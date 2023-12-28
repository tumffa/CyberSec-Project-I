from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from convoapp.models import Post

class Command(BaseCommand):
    def handle(self):
        users = {
            'bob': 'squarepants',
            'alice': 'redqueen',
            'patrick': 'asteroid',
        }

        messages = {
            'bob': 'Hi guys',
            'alice': 'Hello, Alice here',
            'patrick': 'this thing is full of flaws...',
        }

        for username, password in users.items():
            User.objects.create_user(username=username, password=password)
            Post.objects.create(username=username, text=messages[username])
