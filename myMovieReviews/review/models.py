from django.db import models

class Review(models.Model) :
    title = models.CharField(max_length=32)
    releasedate = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    grade = models.DecimalField(max_digits=2, decimal_places=1)
    runningtime = models.IntegerField(default=0)
    runningtimehour = models.IntegerField(default=0)
    runningtimeminute = models.IntegerField(default=0)
    content= models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32, default="Unknown")
    
    