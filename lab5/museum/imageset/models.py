from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def problem_id(self):
        return self.id


class Rectangle(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    X = models.IntegerField(default=0)
    Y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=100)


class UserToImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

