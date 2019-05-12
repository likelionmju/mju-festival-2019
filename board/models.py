from django.db import models
from django.conf import settings

class Board(models.Model):
    PURPOSE_CHOICES = (
        ('속보', '[속보]'),
        ('택시', '[택시]'),
        ('합석', '[합석]'),
        ('기타', '[기타]'),
    )

    title = models.CharField(max_length=50) 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, default=1)
    pub_date = models.DateTimeField('publish')
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField()
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES, default='기타')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:30]