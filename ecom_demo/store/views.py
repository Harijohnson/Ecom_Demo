from django.shortcuts import render
# from django.http import 

# Create your views here.
def store(request):
    context={}
    return render(request,"store/store.html",context=context)