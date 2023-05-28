from django.db import models
from django.contrib.auth.models import User
class Furnitures(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    furjson = models.JSONField()

class Furniture1(models.Model):
    usern= models.CharField(max_length=50)
    furn=models.JSONField()