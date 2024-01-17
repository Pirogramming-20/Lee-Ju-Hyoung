from django.db import models
from apps.devtool.models import DevTool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    image = models.ImageField('이미지', blank=True, upload_to='idea/%Y%m%d')
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, verbose_name = '예상 개발툴')
    select = models.BooleanField('찜하기', default=False)