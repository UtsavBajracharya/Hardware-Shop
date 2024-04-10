from django.db import models
from db_connection import db

# Create your models here.
online_orders= db['online_orders']
inventory_data= db['products']
product_orders= db['product_orders']

