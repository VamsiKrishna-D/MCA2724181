from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Order

def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(name__icontains=query)
    categories = Category.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)
    return render(request, 'catalog/cart.html', {'products': products})

@login_required
def place_order(request):
    cart = request.session.get('cart', [])
    if cart:
        order = Order.objects.create(user=request.user)
        order.products.set(cart)
        order.save()
        request.session['cart'] = []
        return redirect('order_history')
    return redirect('product_list')

@login_required
def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect('product_list')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'catalog/order_history.html', {'orders': orders})

@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', [])
    pk = int(pk)  # ensure pk is an int, if needed
    if pk in cart:
        cart.remove(pk)  # removes one occurrence of pk from the list
        request.session['cart'] = cart
    return redirect('view_cart')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})

@login_required(login_url='login')
def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(name__icontains=query)
    categories = Category.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products, 'categories': categories})


def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('product_list')
    else:
        return redirect('login')