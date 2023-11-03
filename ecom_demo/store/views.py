
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
from store.forms import NewUserCreationForm





# Create your views here.
def store(request):
    # if request.user.is_authenticated:
    #     # User is logged in
    #     # You can access user attributes like request.user.username, request.user.email, etc.
    #     # Perform actions for authenticated users here
    #     return HttpResponse('You are logged in as ' + request.user.email)
    # else:
    #     # User is not logged in
    #     # Perform actions for anonymous users here
    #     return HttpResponse('You are not logged in')
    context={}
    return render(request,"store/store.html",context=context)
    

def product_info(request):
    context={}
    return render(request,"store/product_info.html",context=context)

#def login_user(request):
    if request.method=='POST':
        context={}
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("user credentials"+email,password)
        user=[]
        # user = MyBackEnd().authenticate(email=email, password=password)
        # user=['harijn72@gmail.com','Harikrishnan1@']
        # print("user is " + str(user))
        if user is not None:
            # login(request,user)
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            # username:user.username
            print('loged in')
            return redirect('store')
            # return render(request,"store/store.html",context=context)

        else:
            context={}
            messages.error(request,"you enterd wormg email or password")
            return render(request,"store/login.html",context=context)
    context={}
    return render(request, 'store/login.html',context=context)


#def logout_user(request):
    context={}
    if request.method== "POST":
        logout(request)
        print('you have loged out successfully')
        messages.success(request,"loged out successfully")
        return redirect('store')
    return render(request, 'store/logout.html',context=context)
#first action   working
#def signin(request):
    # print(request.method)
    if request.method== "POST":
        print('you are in')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user=[]
        # my_user = user_info.objects(username=username,email=email,password=password)
        my_user.save()
        context={}
        return redirect("login_user")
        # return render(request,'store/login.html',context=context)
    else:
        print('method is worng')
        context={}
        return render(request,'store/signin.html',context=context)


def signup_user(request):
    if request.method=='POST':
        # form =  NewUserCreationForm(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
        # if form.is_valid():
        #     user = form.save()
        #     return redirect('login_user')
        #my_user.fname     this is for adding single  object to the db
        if User.objects.filter(username=username):
            messages.error(request,"user is already exist please try another user name")
            print('user is already exist please try another user name')
            return redirect('store')
        

        if User.objects.filter(email=email):
            messages.error(request,"Email alread exists")
            print('Email alread exists')    
            return redirect('store')
        
        if len(username)>100:
            messages.error(request,"Username is too long")
            print('Username is too long')
            return redirect('store')
        
        if password != cpassword:
            messages.error(request,"Password does not match")
            print('Password does not match')
            return redirect('store')
        
        if not username.isalnum():
            messages.error(request,"Username not be a number")
            print('Username not be a number')
            return redirect('store')
        

        my_user = User.objects.create_user(username,email,password)
        my_user.is_active =False
        my_user.save()


        #welcome email
        subject = "Welcome to django app"

        message = 'hello '+my_user.username+' !! \n' +'welcome to test django application'
        from_email = EMAIL_HOST_USER
        to_list =[my_user.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        
        #email conformation 

        current_site = get_current_site(request)

        email_subject = "Confermation mail for user creation"

        email_message = render_to_string('email_confermation.html',{
            'name' :my_user.username,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': genarate_token.make_token(my_user),
        })
        
        email_send = EmailMessage(
            email_subject,
            email_message,
            EMAIL_HOST_USER,
            [my_user.email],
        )

        email_send.fails=True
        email_send.send()
        

        # from_email = EMAIL_HOST_USER
        # to_list =[my_user.email]
        # send_mail(subject,message,from_email,to_list,fail_silently=True)
        






        # 'Hello '+my_user.username+" here is the link click to activate your account "

        return redirect("store")


    context= {}
    return render(request,'store/signup_user.html',context=context) 



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username)
        # print(password)
        user= authenticate(request,username=username,password=password)
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
























































