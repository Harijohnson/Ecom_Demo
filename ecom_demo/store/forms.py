from django import forms
from store.models import user_info


class add_user(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ['username','email','password']

# class create_user(forms.ModelForm):
#     username = forms.CharField(max_length = 200)  
#     email = forms.CharField(max_length = 200)    
#     password = forms.CharField(widget = forms.PasswordInput())