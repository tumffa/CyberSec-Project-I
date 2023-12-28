from django.db import migrations, models
from convoapp.models import Post
from django.contrib.auth.models import User


def create_users_and_messages(apps, schema_editor):
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

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
        migrations.RunPython(create_users_and_messages),
    ]