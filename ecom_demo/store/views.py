from django.shortcuts import render
# from django.http import 

# Create your views here.
def store(request):
    context={}
    return render(request,"store/store.html",context=context)


def product(request):
    context={}
    return render(request,"store/product_info.html",context=context)


def login(request):
    context={}
    return render(request, 'store/login.html',context=context)

def signup(request):
    context={}
    return render(request, 'store/signup.html',context=context)

def signout(request):
    context={}
    return render(request, 'store/signout.html',context=context)