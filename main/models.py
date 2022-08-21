from django.db import models

class Movie_model(models.Model):
     title=models.CharField('title',max_length=50)
     rating=models.FloatField('rating')
     year=models.IntegerField('year')
     director=models.CharField('director',max_length=50)
     description=models.TextField()

     def __str__(self):
        return self.title