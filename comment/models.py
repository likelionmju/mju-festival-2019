from django.db import models
from django.conf import settings
from board.models import Board
from lost_property.models import Lost

# Create your models here.
class BoardComment(models.Model):
    title = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, default=1)
    pub_date = models.DateTimeField('publish')
    content = models.TextField()

    def __str__(self):
        return self.content[:20]

class LostComment(models.Model):
    title = models.ForeignKey(Lost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, default=1)
    pub_date = models.DateTimeField('publish')
    content = models.TextField()
    
    def __str__(self):
        return self.content[:20]