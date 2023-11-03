# from django.contrib import admin
# from store.models import user_info

# # Register your models here.
# class user_admin(admin.ModelAdmin):
#     list=['username','email','password']

# admin.site.register(user_info, user_admin)




from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'password']

admin.site.register(CustomUser, CustomUserAdmin)
