"""Declare models for YOUR_APP app."""

from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager
from django.db import models
#creat anew user

class MyAccountManager(BaseUserManager):
    

    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have an Username. ')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
        )
        user.is_admin =True
        user.is_staff =True
        user.is_superuser =True
        user.save(using=self._db)
        return user
    


def get_profile_image_filepath(self):
    return f'profile_image/{str(self.pk)}/{"profile_image.png"}'


def get_default_profile_image():
    return "images/defult.png"

class Account(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email',max_length=60,unique=True,)
    username = models.CharField(max_length=50,unique=False) 
    date_joined = models.DateTimeField(verbose_name='date joined' ,auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login' ,auto_now=True)
    is_admin  = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    profile_image  = models.ImageField(max_length=225,upload_to=get_profile_image_filepath ,null= True,blank=True,default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


    def has_perm(self,perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/'):]

    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        blank=True,
        help_text='Specific permissions for this user.'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )