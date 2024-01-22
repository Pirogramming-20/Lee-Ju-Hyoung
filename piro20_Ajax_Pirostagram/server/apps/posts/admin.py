from django.contrib import admin
from apps.posts import models

admin.site.register(models.Post)
admin.site.register(models.Comment)
