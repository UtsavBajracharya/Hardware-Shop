from django.db import models
from db_connection import db


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

user_final = db['user']