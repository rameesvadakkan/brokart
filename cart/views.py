from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from .cart import Cart

# 🛒 Add product to cart
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

# 🗑️ Remove product from cart
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

# 🛍️ Show cart details
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

