from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def Login(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    result = list(user_data.find({'username':userName,'password':passWord}))
    if len(result) != 0:       
        return redirect(reverse('LandingPage')) # render(request, "LandingPage.html")
    else:
        script = """
        <script>
            alert('Invalid Login Credentials!');
            window.location.href = "login";
        </script>
        """
        return HttpResponse(script)

def RedirectLogin(request):
    return render(request, "login.html")

def LandingPage(request):
    # pending orders
    pending_orders = list(online_orders.find({"status": "Pending"}))
    for order in pending_orders:
        for item in order['order_items']:
            product_details = get_product_details(item['product_id'])
            if product_details:
                item['product_name'] = product_details.get('product_name', 'Unknown')
                item['available_quantity'] = product_details.get('quantity', 0)
    # pending orders

    # low inventory
    query = {'quantity': {'$lt': 8}}
    threshold_data_1 = threshold_data.find()
    product_ids=[]
    for item in threshold_data_1:
        if item['threshold_quantity'] < item['available_quantity']:
            product_ids.append(item['product_id'])
    inventory_data_1 = inventory_data.find(query)
    # low inventory

    # best and less selling
    sellers_data = list(online_orders_data.find())
    sell_products = []
    sell_categories = []

    products = list(inventory_data.find())
    
    for item in sellers_data:
        for order in item['order_items']:
            product = inventory_data.find_one({"product_id": order['product_id']})
            
            if product['category'] not in sell_categories : 
                sell_categories.append(product['category'])

            if product not in sell_products : 
                sell_products.append(product)
    
    for item in sellers_data:
        for order in item['order_items']:
            for item in sell_products:
                if item['product_id'] == order['product_id']:
                    if 'ordered_quantity' in item:
                        item['ordered_quantity'] += order['ordered_quantity']
                    else:
                        item['ordered_quantity'] = order['ordered_quantity']

    less_selling = []

    for product in products:
        if product not in sell_products:
            less_selling.append(product)
    # best and less selling

    return render(request, 'LandingPage.html', 
                  {
                      'pending_orders': pending_orders, 
                      'low_inventory': inventory_data_1,
                      'sell_categories': sell_categories,
                      'sell_products': sell_products, 
                      'less_selling': less_selling
                   }
                  )


def get_product_details(product_id):
    product_collection = db['products']  # Replace 'products' with your actual collection name
    product = product_collection.find_one({'product_id': product_id})
    return product
