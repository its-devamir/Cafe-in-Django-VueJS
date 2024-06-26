from django.shortcuts import render, redirect
from .models import Product, Order, Storage, User
from django.http import JsonResponse


def home(request):
    top_selling_products = Product.objects.all()[:12]  # Simplified for brevity
    return render(request, 'cafe/home.html', {'top_selling_products': top_selling_products})

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['usernameOrEmail']
        password = request.POST['password']
        if username_or_email == "admin" and password == "admin":
            return redirect('admin_panel')
        # Add logic for other users
    return render(request, 'cafe/login.html')

def signup(request):
    if request.method == 'POST':
        # Save the user details
        pass
    return render(request, 'cafe/signup.html')

def products(request):
    # Add logic to display products
    return render(request, 'cafe/products.html')

def admin_panel(request):
    # Add logic for admin panel
    return render(request, 'cafe/admin_panel.html')

def manage_storage(request):
    # Add logic for managing storage
    return render(request, 'cafe/manage_storage.html')

def add_product(request):
    if request.method == 'POST':
        # Add product to database
        pass
    return render(request, 'cafe/add_product.html')

def cart(request):
    # Add logic for cart
    return render(request, 'cafe/cart.html')

def orders(request):
    # Add logic for orders
    return render(request, 'cafe/orders.html')







def top_selling_products_api(request):
    top_selling_products = Product.objects.all()[:12]
    products_data = [{'name': product.name, 'price': product.price, 'image': product.image.url} for product in top_selling_products]
    return JsonResponse(products_data, safe=False)
