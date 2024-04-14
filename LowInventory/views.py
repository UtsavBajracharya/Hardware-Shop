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
    less_qty_product = []
    threshold_data_1 = threshold_data.find()
    product_ids = []
    for item in threshold_data_1:
        available_quantity = inventory_data.find({"product_id": item["product_id"]})
        if item['threshold_quantity'] < int(list(available_quantity)[0]["quantity"]):
            product_ids.append(item['product_id'])
    # inventory_data_1 = inventory_data.find(query)
    default_threshold_products = inventory_data.find({'product_id': {'$nin': product_ids}, 'quantity': {'$lt': 10}})
    less_qty_product.extend(default_threshold_products)
    ordered_product = product_orders_data.find()
    less_qty_product = [data for data in less_qty_product if data['product_id'] not in ordered_product]

    # still working here April 13, 9.45 AM
    return render(request,'LowInventory.html',{'inventory_data':list(less_qty_product)})

def setThreshold(request):
    product_id = request.POST["productNumber"]
    threshold_quantity = int(request.POST["thresholdQuantity"])
    threshold_data.update_one({"product_id":int(product_id)},{"$set":{"threshold_quantity":threshold_quantity}})
    # product_numbers =[]
    # threshold_product_data = threshold_data.find()
    # for item in threshold_product_data:
    #     product_numbers.append(item["product_id"])
    # print("RAAAHUL")
    # print(product_numbers)  
    # # if product_id 
    return HttpResponse("Updated")
