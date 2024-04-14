
mongoimport --db='hardware_shop' --collection='products' --file='/tmp/products.json' --jsonArray --username='root' --password='root' --authenticationDatabase=admin

mongoimport --db='hardware_shop' --collection='product_orders' --file='/tmp/product_orders.json' --jsonArray --username='root' --password='root' --authenticationDatabase=admin

mongoimport --db='hardware_shop' --collection='online_orders' --file='/tmp/online_orders.json' --jsonArray --username='root' --password='root' --authenticationDatabase=admin

mongoimport --db='hardware_shop' --collection='customers' --file='/tmp/customers.json' --jsonArray --username='root' --password='root' --authenticationDatabase=admin

mongoimport --db='hardware_shop' --collection='vendors' --file='/tmp/vendors.json' --jsonArray --username='root' --password='root' --authenticationDatabase=admin
