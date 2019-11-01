from django.db import models

class UserInfo(models.Model):
    user_name=models.CharField(max_length=32)
    user_password=models.CharField(max_length=32)
    user_email=models.CharField(max_length=64)

# Create your models here.
