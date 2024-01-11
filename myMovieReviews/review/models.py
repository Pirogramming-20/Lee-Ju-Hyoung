from django.db import models

class Review(models.Model) :
    title = models.CharField(max_length=32)
    releasedate = models.DateTimeField(auto_now=False)
    genre = models.CharField(max_length=32)
    grade = models.DecimalField(max_digits=2, decimal_places=1)
    runningtime = models.IntegerField(default=0)
    content= models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32, default="Unknown")
    
    