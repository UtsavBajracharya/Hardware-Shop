from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import render

def Billing(request):
    return render(request, 'Billing.html')
def Dashboard(request):
    return render(request, 'Dashboard.html')
def LandingPage(request):
    return render(request, 'LandingPage.html')
def LowInventory(request):
    return render(request, 'LowInventory.html')
def OnlineOrders(request):
    return render(request, 'OnlineOrders.html')
def Prediction(request):
    return render(request, 'Prediction.html')
def ProductOrders(request):
    return render(request, 'ProductOrders.html')
def Sales(request):
    return render(request, 'Sales.html')
def Inventory(request):
    return render(request, '.\HTML/Inventory.html')