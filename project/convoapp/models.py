from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        db_table = 'Posts'

