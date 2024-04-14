from datetime import datetime
import random
from urllib.parse import parse_qs
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import random

# Create your views here.
def Contact(request):
    return render(request, 'Contact.html')
    
