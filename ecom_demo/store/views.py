
from django.shortcuts import render,redirect
# from django.http import 
from django.contrib.auth.models import User   # to update the data into db
from django.contrib import messages
# from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, logout , authenticate
# from store.backends import MyBackEnd
# from store.models import user_info
# from store.forms import add_user # create_user
# from store.backends import 
from django.http import HttpResponse

from ecom_demo.settings import *
from django.core.mail import send_mail,EmailMessage  
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.utils.encoding import force_bytes,force_str
from store.token import genarate_token
# from email.message import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode    
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from store.forms import RegistrationForm,AccountAuthentication
from django.http import HttpResponse



# Create your views here.
def store(request):
    context={}
    return render(request,"store/store.html",context=context)
    

def product_info(request):
    context={}
    return render(request,"store/product_info.html",context=context)


def signup_user(request,*args,**kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect('store')
    

    context={}


    if request.method == 'POST':
        form  = RegistrationForm(request.POST)
        print('you are inside the post request')
        print(form.is_valid())
        if form.is_valid():
            # user= form.save(commit=False)
            # user.is_active =False   # now it is true for development server 
            print('you are inside the the valid form')
            form.save()

            '''email = form.cleaned_data.get('email').lower()
            username = form.cleaned_data.get('username')
            #welcome email
            subject = "Welcome to django app"

            message = 'hello '+username+' !! \n' +'welcome to test django application'
            from_email = EMAIL_HOST_USER
            to_list =[email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            
            #email conformation 

            current_site = get_current_site(request)

            email_subject = "Confermation mail for user creation"

            email_message = render_to_string('email_confermation.html',{
                'name' :username,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(form.pk)),
                'token': genarate_token.make_token(form),
            })
            
            email_send = EmailMessage(
                email_subject,
                email_message,
                EMAIL_HOST_USER,
                [email],
            )
            email_send.fails=True
            email_send.send()'''
            return redirect("login_user")

        else:
            form = RegistrationForm()
            context['registration_form'] =  form
    return render(request,'store/signup_user.html',context=context) 



def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # print(username)
        # print(password)
        user= authenticate(request,email=email,password=password)
        # print(user)
        # print('look above')
        if user is not None:
            login(request,user)
            messages.success(request,'Loged out Successfully')
            return redirect('store')
        else:
            messages.error(request,"Username or Password is Incorrect")
            print('user cred is not valid')
            return redirect('login_user')
    return render(request,'store/login_user.html') 



def logout_user(request):
    if request.method == 'POST':
        messages.success(request,'Loged out Successfully')
        logout(request)
       
        return redirect('store')
    return render(request,'store/logout_user.html')

def activate(request, uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        my_user = None
    if my_user is not None and genarate_token.check_token(my_user,token):
        my_user.is_active=True
        my_user.save()
        login(request,my_user)
        return redirect('store')
    else:
        return render(request,'activation_failed.html')
























































