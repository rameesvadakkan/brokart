from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.db.models import Q
from django.core.paginator import Paginator

@login_required

def add_product(request):
    if request.method == 'POST':
       form = ProductForm(request.POST,request.FILES)
       if form.is_valid():
           product = form.save(commit=False)
           product.created_by = request.user
           product.save()
           return redirect('product_list')
    else:
        form = ProductForm()
    return render(request,'products/add_product.html', {'form': form})

def product_list(request,category_slug=None):
    categories = Category.objects.all()
    query = request.GET.get('q')
    sort = request.GET.get('sort', 'latest')  # default sorting
    products = Products.objects.all().order_by('-created_at')
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None
    
      # 🔍 filter by search
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
     # 🔹 Sorting logic
    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')
    else:  # latest
        products = products.order_by('-created_at')

    # 🔹 Pagination (6 per page)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)    

    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products,
        'selected_category': category,
        'query': query,
        'sort': sort,
    })    

    return render(request,'products/product_list.html',{'products':products})

def product_details(request,pk):
    product = get_object_or_404(Products,pk=pk)
    return render(request,'products/product_details.html',{'product':product})
    

