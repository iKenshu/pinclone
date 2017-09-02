from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Pin(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='img/pins')

    def __str__(self):
        return self.title