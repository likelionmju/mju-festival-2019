from django.db import models

# Create your models here.
class Lost(models.Model):
    title = models.CharField(max_length=50) 
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField('publish')
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField() 
    password = models.CharField(max_length=20)
    found = models.BooleanField(default=False)

    def __str__(self):
        return self.title