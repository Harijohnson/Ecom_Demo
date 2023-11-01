from django.shortcuts import render,redirect
# from django.http import 
from django.contrib.auth.models import User   # to update the data into db
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login, logout
# from store.backends import MyBackEnd
from store.models import user_info
# from store.forms import add_user # create_user
# from store.backends import 

# Create your views here.
def store(request):
    context={}
    return render(request,"store/store.html",context=context)
    
#first action   working
def signin(request):
    # print(request.method)
    if request.method== "POST":
        print('you are in')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = user_info.objects.create(username=username,email=email,password=password)
        my_user.save()
        context={}
        return render(request,'store/login.html',context=context)
    else:
        print('method is worng')
        context={}
        return render(request,'store/signin.html',context=context)

def product(request):
    context={}
    return render(request,"store/product_info.html",context=context)

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("user credentials"+email,password)
        user = authenticate(email=email, password=password)
        user=['harijn72@gmail.com','Harikrishnan1@']
        print(user)
        if user is not None:
            login(request,user)
            username:user.username
            return render(request,"store/store.html",context=context)
        else:
            context={}
            messages.error(request,"you enterd wormg email or password")
            return render(request,"store/login.html",context=context)



    context={}
    return render(request, 'store/login.html',context=context)


# def signout(request):
#     context={}
#     return render(request, 'store/signout.html',context=context)
