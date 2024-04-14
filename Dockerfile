# Dockerfile

FROM mongo:7.0.2
ENV MONGO_INITDB_ROOT_USERNAME root
ENV MONGO_INITDB_ROOT_PASSWORD root
ENV MONGO_INITDB_DATABASE testdb

COPY Database/customers.json /tmp/customers.json
COPY Database/online_orders.json /tmp/online_orders.json
COPY Database/product_orders.json /tmp/product_orders.json
COPY Database/products.json /tmp/products.json
COPY Database/vendors.json /tmp/vendors.json

COPY importscript.sh /docker-entrypoint-initdb.d/

ADD init-mongo.js /docker-entrypoint-initdb.d/

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11-slim

# Allows docker to cache installed dependencies between builds
WORKDIR F:\Lambton_College\My_Folder\sem2\PythonProject\w24PYTHONProject_TechArmy
COPY . .
# COPY entrypoint.sh /
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "./manage.py"]
# ENTRYPOINT ["/entrypoint.sh"]
CMD ["runserver", "0.0.0.0:8000"]

