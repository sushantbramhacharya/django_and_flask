from django.shortcuts import render

def home(request):
    products = [
        {"name": "Product 1", "price": 10.00},
        {"name": "Product 2", "price": 20.00},
        {"name": "Product 3", "price": 30.00},
        {"name": "Product 4", "price": 40.00},
        {"name": "Product 5", "price": 50.00},
    ]
    return render(request,"index.html",{'products':products})