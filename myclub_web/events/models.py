from django.db import models

# # Create your models here.

class Myuser(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.fullname


