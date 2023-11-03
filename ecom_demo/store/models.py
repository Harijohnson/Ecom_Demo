# from django.db import models

# Create your models here.

#  no need for this in future 
# class user_info(models.Model):
#     username=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100,primary_key=True)
#     password=models.CharField(max_length=50)

#     def __str__(self):
#        return self.email
        
#     # class Meta:
#     #    ordering = ('username')


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username=models.CharField(max_length=150,primary_key=True)
    email = models.EmailField(max_length=100,unique=True)
    address = models.CharField(max_length=500)
    # Add any additional fields you want

    def __str__(self):
        return self.username


