# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11-slim

# Allows docker to cache installed dependencies between builds
WORKDIR F:\Lambton_College\My_Folder\sem2\PythonProject\w24PYTHONProject_TechArmy
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

