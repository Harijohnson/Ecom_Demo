from django.db import models

# Create your models here.
class user_info(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50)

    def __str__(self):
       return self.email
        