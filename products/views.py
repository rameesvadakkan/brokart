from django.shortcuts import render, get_object_or_404
from .models import Products
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required


def product_list(request):
    products = Products.objects.all()
    return render(request,'products/product_list.html',{'products':products})

def product_details(request,pk):
    product = get_object_or_404(Products,pk=pk)
    return render(request,'products/product_details.html',{'product':product})
    

