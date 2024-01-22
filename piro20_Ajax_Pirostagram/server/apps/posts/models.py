from django.db import models
from apps.users.models import User

class Post(models.Model) :
    image = models.ImageField('이미지', blank=True, upload_to='post/%Y%m%d')
    like = models.IntegerField('좋아요', default=0)
    content = models.TextField('글 내용')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = '작성자')

class Comment(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = '작성자')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField() 