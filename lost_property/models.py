from django.db import models
from django.conf import settings

# Create your models here.
class Lost(models.Model):
    title = models.CharField(max_length=50) 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish')
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField() 
    password = models.CharField(max_length=20)
    found = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:30]