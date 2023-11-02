from django.shortcuts import render,redirect
# from django.http import 
from django.contrib.auth.models import User   # to update the data into db
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, logout
from store.backends import MyBackEnd
from store.models import user_info
# from store.forms import add_user # create_user
# from store.backends import 
from django.http import HttpResponse


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
    

def product(request):
    
    context={}
    return render(request,"store/product_info.html",context=context)

def login_user(request):
    if request.method=='POST':
        context={}
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("user credentials"+email,password)
        user = MyBackEnd().authenticate(email=email, password=password)
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


def logout_user(request):
    context={}
    if request.method== "POST":
        logout(request)
        print('you have loged out successfully')
        messages.success(request,"loged out successfully")
        return redirect('store')
    return render(request, 'store/logout.html',context=context)
#first action   working
def signin(request):
    # print(request.method)
    if request.method== "POST":
        print('you are in')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = user_info.objects(username=username,email=email,password=password)
        my_user.save()
        context={}
        return redirect("login_user")
        # return render(request,'store/login.html',context=context)
    else:
        print('method is worng')
        context={}
        return render(request,'store/signin.html',context=context)
