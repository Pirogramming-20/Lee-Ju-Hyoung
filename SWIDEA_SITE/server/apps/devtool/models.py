from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField('이름', max_length=24)
    kind = models.CharField('종류', max_length=24)
    content = models.TextField('개발툴 설명', max_length=24)
    def __str__(self):
        return f'{self.name}'
    