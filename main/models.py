from django.db import models


class Movie_model(models.Model):
    title = models.CharField('title', max_length=50)
    rating = models.FloatField('rating')
    year = models.IntegerField('year')
    director = models.CharField('director', max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.CharField('link', max_length=200)
    visit_count = models.IntegerField('count', default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    name_user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    movie = models.ForeignKey(Movie_model, on_delete=models.CASCADE)

    def __str__(self):
         return self.name_user