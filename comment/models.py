from django.db import models
from board.models import Board
from lost_property.models import Lost

# Create your models here.
class Board(models.Model):
    title = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    pub_date = models.DateTimeField('publish')
    author = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Lost(models.Model):
    title = models.ForeignKey(Lost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    pub_date = models.DateTimeField('publish')
    author = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
