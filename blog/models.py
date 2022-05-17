from datetime import datetime

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField()
    full_description = models.TextField()
    featured_image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
