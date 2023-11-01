from django.shortcuts import render,redirect
# from django.http import 
from django.contrib.auth.models import User   # to update the data into db
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from store.models import user_info
from store.forms import add_user # create_user


# Create your views here.
def store(request):
    context={}
    return render(request,"store/store.html",context=context)

def signin(request):
    '''print(request.POST.get('username'))
    print('good you are called by html ')
    print(request.method)
    if request.method=='POST':
        username =  request.POST.get('username')
        #another way to get the user information from the html
        # username =  request.POST['username']

        email= request.POST.get('email')
        password= request.POST.get('password')
        cPassword= request.POST.get('cPassword')
        print(username)
        print(email)
        print(password)
        print(cPassword)'''

        # my_user =User.objects.create_user(username=username, email=email, password=password)
        #we can add anothe objects as below
        #my_user.f_name=fname        
        #update users in created database user
        # my_user = create_user(username=username, email=email, password=password)
        #'''my_user = add_user(username=username, email=email, password=password)
    #     my_user.save()'''
        
    #     # to show some information about acount creation 
    #     # messages.success(request,"Account Created Successfully")

    #     '''context=my_user
    #     return render(request,"store/signin.html",context=context)
    # else:
    #     print('nothing happened')'''
    
    context={'form':add_user()}
    return render(request,"store/signin.html",context=context)



#first action 
# def signin(request):
    print('good you are called by html ')
    if request.method=='POST':
        username =  request.POST.get('username')
        #another way to get the user information from the html
        # username =  request.POST['username']

        email= request.POST.get('email')
        password= request.POST.get('password')
        cPassword= request.POST.get('cPassword')


        my_user =User.objects.create_user(username=username, email=email, password=password)
        #we can add anothe objects as below
        #my_user.f_name=fname        
        #update users in created database user
        my_user = create_user(username=username, email=email, password=password)
        my_user.save()
        
        # to show some information about acount creation 
        # messages.success(request,"Account Created Successfully")

        context=my_user
        return render(request,"store/signin.html",context=context)
    # context={}
    # return render(request,"store/signin.html",context=context)

        # return render(request, 'templates/store/store.html',context=context)




#     # context={}
#     # return render(request, 'store/signup.html',context=context)






def product(request):
    context={}
    return render(request,"store/product_info.html",context=context)

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request,user)
            username:user.username
            return redirect("home")
        else:
            context={}
            messages.error(request,"you enterd wormg email or password")
            return render(request,"store/login.html",context=context)



    context={}
    return render(request, 'store/login.html',context=context)


# def signout(request):
#     context={}
#     return render(request, 'store/signout.html',context=context)
