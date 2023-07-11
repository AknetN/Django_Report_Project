python3 -m venv env
source env/bin/activate
pip install django 
pip install --upgrade pip
pip install djangorestframework
pip freeze > requirements.txt 
django-admin startproject report_pr .
python3 manage.py startapp report_app 



python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


python3 manage.py createsuperuser



# **Building a Simple API with Django REST Framework**

## **Description**
Your task is to create a simple API using Django REST Framework (DRF) that allows users to manage a collection of tasks. The API should support basic CRUD (Create, Read, Update, Delete) operations on the task collection. Each task should have attributes such as title, description, priority, and completion status.

You should use Django ORM to define the Task model and write the necessary serializers and views to handle API requests. The API endpoints should follow RESTful conventions and should support JSON format for data exchange.

## **Examples:**

## **Endpoint:**

### **POST /api/tasks/**


### **Request body:**

```python 
{
    "title": "Complete project report",
    "description": "Write a detailed report on the project progress.",
    "priority": "High",
    "completed": false
}
```
### **Response body:**
```python 
{
    "id": 1,
    "title": "Complete project report",
    "description": "Write a detailed report on the project progress.",
    "priority": "High",
    "completed": false
}
``` 
### **Retrieve a task by ID:**
​
### **Endpoint: GET /api/tasks/{id}/**
### **Response body:**
```python 
{
    "id": 1,
    "title": "Complete project report",
    "description": "Write a detailed report on the project progress.",
    "priority": "High",
    "completed": false
}
``` 
### **Update a task:**
​
### **Endpoint: PUT /api/tasks/{id}/**
### **Request body:**
```python 
{
    "title": "Complete project report (Revised)",
    "description": "Write a detailed report on the project progress with updated findings.",
    "priority": "High",
    "completed": false
}
```
### **Response body:**
```python 
{
    "id": 1,
    "title": "Complete project report (Revised)",
    "description": "Write a detailed report on the project progress with updated findings.",
    "priority": "High",
    "completed": false
}
```
### **Delete a task:**
​
### **Endpoint: DELETE /api/tasks/{id}/**
### **Response body: Empty**
