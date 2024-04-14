import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import random


class OnlineOrder:
    def __init__(self, order_id, customer_name, status ):
        self.order_id = int(order_id)
        self.customer_name = customer_name
        self.status = status

        

def get_product_details(product_id):
    product_collection = db['products']  # Replace 'products' with your actual collection name
    product = product_collection.find_one({'product_id': product_id})
    return product


def OnlineOrders(request):
    online_orders1 = list(online_orders.find())
    for order in online_orders1:
        for item in order['order_items']:
            product_details = get_product_details(item['product_id'])
            if product_details:
                item['product_name'] = product_details.get('product_name', 'Unknown')
                item['available_quantity'] = product_details.get('quantity', 0)
    return render(request, 'OnlineOrders.html', {'online_orders': online_orders1})



class OrderItem:
    def __init__(self, product_id, ordered_quantity, product_name, available_quantity):
        self.product_id = product_id
        self.ordered_quantity = ordered_quantity
        self.product_name = product_name
        self.available_quantity = available_quantity

def parse_order_items(order_items_data):
    order_items = []
    for item_data in order_items_data:
        product_id = item_data.get('product_id')
        ordered_quantity = item_data.get('ordered_quantity')
        product_name = item_data.get('product_name')
        available_quantity = item_data.get('available_quantity')
        order_item = OrderItem(product_id, ordered_quantity, product_name, available_quantity)
        order_items.append(order_item)
    return order_items

def orderShipped(request):
    updatedRowsList=handle_ajax_request(request)
    
    for document in updatedRowsList:
        record = OnlineOrder(document['order_id'],document['customer_name'],document['status'])
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        product_numbers = online_orders.find({'order_id':int(record['order_id'])})
        order_items=[]
        for items in product_numbers:
            order_items = items['order_items']
        for item in order_items:
            on_hand = inventory_data.find({'product_id':int(item['product_id'])})
            ordered_quantity = int(item['ordered_quantity'])
            for details in on_hand:
                on_hand_1=[]
                on_hand_1.append(details)
                product=on_hand_1[0]
                prod=int(product['product_id'])               
                remaining_on_hand=int(product['quantity'])-ordered_quantity
                inventory_data.update_one({'product_id':prod},{"$set":{'quantity': remaining_on_hand}})

                

        online_orders.update_one({'order_id':int(record['order_id'])},{"$set":{'status': 'Processed'}})
        # inventory_data.updae_on/e('product_id':int)
    return HttpResponse("request")

def cancelOrders(request):
    updatedRowsList=handle_ajax_request(request)
    for document in updatedRowsList:
        record = OnlineOrder(document['order_id'],document['customer_name'],document['status'])
        record = json.loads(json.dumps(record.__dict__)) #converting the object to a string first then to a dict
        online_orders.update_one({'order_id':int(record['order_id'])},{"$set":{'status': 'Cancelled'}})
       
    return HttpResponse("request")


# def handle_ajax_request(request):
#     if request.method == 'POST':
#         # Assuming the AJAX request sends JSON data
#         json_string = request.body.decode('utf-8')  # Get the JSON string from the request

#         # Parse the JSON string into a Python data structure
#         data = json.loads(json_string)
#         # Iterate through the data
#         updatedRowsList = []
#         for item in data:
#             record={
#         "order_id":item['Order ID'],
#         "customer_name":item['Customer Name'],
#         "status":item['Status'],
#         "order_items":item.get('order_items',[])
        
#     }
#             updatedRowsList.append(record)

#         # You can then process the data as needed
#         # For example, you might want to return a JSON response
#         return updatedRowsList

def handle_ajax_request(request):
    if request.method == 'POST':
        # Assuming the AJAX request sends JSON data
        json_string = request.body.decode('utf-8')  # Get the JSON string from the request

        # Parse the JSON string into a Python data structure
        data = json.loads(json_string)
        
        # Iterate through the data
        updatedRowsList = []
        for item in data:
            record = {
                "order_id": item['Order ID'],  # Use 'order_id' instead of 'Order ID'
                "customer_name": item['Customer Name'],  # Use 'customer_name' instead of 'Customer Name'
                "status": item['Status'],  # Use 'status' instead of 'Status'
            }

            updatedRowsList.append(record)

        return updatedRowsList
















def dummyOrders(request):
   
# Dummy inventory data
    inventory_data = [
        {
            "product_id": 1000074,
            "product_name": "Hose Reel Cart",
            "quantity": 8,
        },
        {
            "product_id": 1000075,
            "product_name": "Watering Wand",
            "quantity": 10,
        },
        {
            "product_id": 1000076,
            "product_name": "Garden Gloves",
            "quantity": 25,
        },
        {
            "product_id": 1000077,
            "product_name": "Watering Can",
            "quantity": 20,
        },
        {
            "product_id": 1000078,
            "product_name": "Garden Tool Set",
            "quantity": 15,
        },
        {
            "product_id": 1000079,
            "product_name": "Garden Hose Repair Kit",
            "quantity": 18,
        },
        {
            "product_id": 1000080,
            "product_name": "Plant Watering Spikes",
            "quantity": 20,
        }
    ]

    # Generate dummy online orders
    num_orders = 3
    orders = []

    for _ in range(num_orders):
        order = {
            "order_id": random.randint(1000, 9999),  # Generate a random order ID
            "customer_name": "Customer " + str(random.randint(1, 100)),  # Random customer name
            "products": []
        }
        
        # Randomly select products from inventory and create order items
        num_items = random.randint(1, 5)  # Random number of items in the order
        for _ in range(num_items):
            product = random.choice(inventory_data)
            ordered_quantity = random.randint(1, min(product["quantity"], 5))  # Random ordered quantity
            order_item = {
                "product_id": product["product_id"],
                "ordered_quantity": ordered_quantity
            }
            order["products"].append(order_item)
        
        orders.append(order)

    # Print dummy orders
    for order in orders:
        print(order)
    
    
