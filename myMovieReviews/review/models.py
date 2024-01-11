from django.db import models

class Review(models.Model) :
    title = models.CharField(max_length=32)
    releasedate = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    garde = models.CharField(max_length=32)
    runningtime = models.CharField(max_length=32)
    content= models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)
    
    