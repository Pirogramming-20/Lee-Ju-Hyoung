from django.contrib import admin
from apps.users import models

admin.site.register(models.User)