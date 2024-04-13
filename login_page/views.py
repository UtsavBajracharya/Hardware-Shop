from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import render
from .models import user_final

# Create your views here.
def login(request):
    return render(request, 'login.html')

def loginCredentialsCheck(request):

    return HttpResponse("Rahul" )

def addUser(request):
    record = {
        "Name": "Rahul",
        "username": "Rahul",
        "password": "Rahul"
    }
    user_final.insert_one(record)
    return HttpResponse("New user added")

def showRecords(request):
    record = user_final.find({},{'name':'Rahul'})
    return HttpResponse(record)

def userAuthentication(request):
    userName = request.GET['username']
    passWord = request.GET['password']
    result = list(user_final.find({'username':userName,'password':passWord}))
    print("Result : ")
    print(result)
    if len(result) != 0:
        return HttpResponse("User Authenticated")
    else:
        return HttpResponse("Authentication Failed")
    
def home(request):
    return render(request,'LandingPage.html')
def Inventory(request):
    return render(request, 'Inventory.html')