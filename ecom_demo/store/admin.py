from django.contrib import admin
from store.models import user_info

# Register your models here.
class user_admin(admin.ModelAdmin):
    list=['name','email','password']

admin.site.register(user_info, user_admin)




