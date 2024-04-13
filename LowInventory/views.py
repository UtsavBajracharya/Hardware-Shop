from datetime import datetime
import random
from urllib.parse import parse_qs
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import random


def lowInventory(request):
    query = {
    'quantity': {
          '$lt': 8
    }
}
    threshold_data_1=threshold_data.find()
    product_ids=[]
    for item in threshold_data_1:
        if item['threshold_quantity']<item['available_quantity']:
            product_ids.append(item['product_id'])
    inventory_data_1 = inventory_data.find(query)
    print('product_ids')
    print(product_ids)
    # still working here April 13, 9.45 AM
    return render(request,'LowInventory.html',{'inventory_data':list(inventory_data_1)})

def setThreshold():

    

    return HttpResponse("Updated")
