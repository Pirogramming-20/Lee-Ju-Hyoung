from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField('아이디', unique=True, max_length=16, null=True)
    password = models.CharField('비밀번호', max_length=16)
    nickname = models.CharField('닉네임', max_length=16, null=True)
    has_liked = models.IntegerField(default = 0)
