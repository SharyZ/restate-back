from datetime import datetime

from django.db import models

# Create your models here.

class Listing(models.Model):
    SALE_TYPE = [
        ('FOR_SALE', 'For sale'),
        ('FOR_RENT', 'For rent'),
    ]

    CITY_CHOICE = [
        ('tashkent', 'Tashkent'),
        ('samarkand', 'Samarkand'),
        ('nukus', 'Nukus'),
    ]

    description = models.TextField()
    price = models.IntegerField(help_text='Price in $ (USD)')
    sale_type = models.CharField(max_length=25, choices=SALE_TYPE, help_text='For rent or sale?')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITY_CHOICE)
    featured_image = models.ImageField(upload_to='listing/')
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-created_at']
