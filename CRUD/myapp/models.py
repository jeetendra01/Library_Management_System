from django.db import models

# Create your models here.
class User(models.Model):
    studentname =models.CharField(max_length=90)
    bookname =models.CharField(max_length=90)
    booknumber =models.CharField(max_length=90)

