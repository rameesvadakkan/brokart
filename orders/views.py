from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart

@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=cart.get_total_price()
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )

        cart.clear()
        return render(request, 'orders/thank_you.html', {'order': order})

    return render(request, 'orders/checkout.html', {'cart': cart})
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})
