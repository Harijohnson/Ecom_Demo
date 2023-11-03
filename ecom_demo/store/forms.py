#from django import forms
# from store.models import user_info


# class add_user(forms.ModelForm):
#     class Meta:
#         model = user_info
#         fields = ['username','email','password']

# class create_user(forms.ModelForm):
#     username = forms.CharField(max_length = 200)  
#     email = forms.CharField(max_length = 200)    
#     password = forms.CharField(widget = forms.PasswordInput())

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create your form in here  this form is not associated with models.py
class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

    def save(self,commit=True):
        user = super(NewUserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user









