from django.db import models
from db_connection import db

# Create your models here.
online_orders= db['online_orders']
inventory_data= db['products']
threshold_data= db['threshold']
online_orders_data = db['online_orders']
product_orders_data = db['product_orders']