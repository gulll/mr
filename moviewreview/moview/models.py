from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    poster = models.ImageField(upload_to='site_media', blank=True)
    rel_date=models.DateTimeField('Date Released')
    director = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=1,decimal_places=1)

class Review(models.Model):
    user = models.CharField(max_length=50)
    rating=models.DecimalField(max_digits=1,decimal_places=1)
    body = models.TextField()
    post_date=models.DateTimeField('Date Reviewed')
    movie =models.ForeignKey(Movie)