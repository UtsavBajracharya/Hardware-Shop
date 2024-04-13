# run this at the beginning and only once
from pymongo import MongoClient
import os
import json

def seed_database():
    client = MongoClient('localhost', 27017)  # Connect to MongoDB server
    db = client.hardware_shop # Create a database named 'hardware_shop'
    db.product_orders.drop()  # Drop the collection if it already exists
    db.products.drop() # Drop the collection if it already exists
    db.online_orders.drop() # Drop the collection if it already exists

    db.create_collection('products')  # Create a new collection named 'products'
    db.create_collection('product_orders')  # Create a new collection named 'product_orders'
    db.create_collection('online_orders')  # Create a new collection named 'online_orders'

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to product_orders.json
    product_json_path = os.path.join(current_dir, 'products.json')

    # Construct the absolute path to product_orders.json
    product_orders_json_path = os.path.join(current_dir, 'product_orders.json')

    # Construct the absolute path to online_orders.json
    online_orders_json_path = os.path.join(current_dir, 'online_orders.json')

    # Open product.json using the absolute path
    with open(product_json_path) as p:
        product_jsondata = json.load(p)

    # Open product_orders.json using the absolute path
    with open(product_orders_json_path) as po:
        product_orders_jsondata = json.load(po)

    # Open online_orders.json using the absolute path
    with open(online_orders_json_path) as onp:
        online_orders_jsondata = json.load(onp)
    
    db.products.insert_many(product_jsondata)
    db.product_orders.insert_many(product_orders_jsondata)
    db.online_orders.insert_many(online_orders_jsondata)

    print("Database and collection created successfully.")

if __name__ == '__main__':
    seed_database()


