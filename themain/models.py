from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Link(models.Model):
    link = models.TextField("silka")
    urgency = models.IntegerField("number_bruh")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.link} {self.urgency}"
