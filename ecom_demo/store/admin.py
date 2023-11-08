from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from store.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin',"is_staff",)  # table headings
    search_fields=('email','username',)   #search the item in the table
    readonly_fields = ('id','date_joined','last_login',)  #after in the click 

    filter_horizontal=()
    list_filter=()
    fieldsets = ()


admin.site.register(Account,AccountAdmin)


