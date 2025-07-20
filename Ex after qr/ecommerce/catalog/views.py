from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_POST
from django.http import HttpResponse  # ✅ This line fixes the error
from django.template.loader import get_template
from xhtml2pdf import pisa  # ✅ Required for generating PDF
from .models import Product, Category, Order
from decimal import Decimal
import qrcode
import io
import base64
from .models import Order
from io import BytesIO

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

@require_POST
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        cart = {}

    quantity = int(request.POST.get('quantity', 1))
    pk_str = str(pk)

    if pk_str in cart:
        cart[pk_str] += quantity
    else:
        cart[pk_str] = quantity

    request.session['cart'] = cart
    request.session.modified = True  
    return redirect('product_list')
    
def view_cart(request):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        cart = {}

    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total = 0

    for product in products:
        quantity = cart.get(str(product.id), 0)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'catalog/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })

@login_required
def place_order(request):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        cart = {}

    if cart:
        order = Order.objects.create(user=request.user)
        product_ids = [int(pid) for pid in cart.keys()]
        order.products.set(product_ids)
        order.save()
        request.session['cart'] = {}
        return redirect('order_history')

    return redirect('product_list')

@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        cart = {}

    pk_str = str(pk)
    if pk_str in cart:
        del cart[pk_str]
        request.session['cart'] = cart

    return redirect('view_cart')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'catalog/order_history.html', {'orders': orders})

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

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == "POST":
        order.delete()
        return redirect('order_history')
    return render(request, 'catalog/order_confirm_delete.html', {'order': order})

@login_required
def generate_invoice_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    products = order.products.all()

    subtotal = sum(product.price for product in products)
    cgst = subtotal * Decimal('0.09')
    sgst = subtotal * Decimal('0.09')
    total = subtotal + cgst + sgst

    context = {
        'order': order,
        'products': products,
        'subtotal': subtotal,
        'cgst': cgst,
        'sgst': sgst,
        'total': total,
    }

    template_path = 'catalog/invoice_template.html'
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_order_{order.id}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def payment_page(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    products = order.products.all()

    subtotal = sum(product.price for product in products)
    cgst = subtotal * Decimal('0.09')
    sgst = subtotal * Decimal('0.09')
    igst = subtotal * Decimal('0.18')
    total = subtotal + cgst + sgst + igst

    upi_id = "9550040711-2@ybl"  # Your UPI ID here
    payee_name = "D VamsiKrishna"

    # Generate UPI payment URI
    qr_data = f"upi://pay?pa={upi_id}&pn={payee_name}&am={total:.2f}&cu=INR"

    # Generate QR code image
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to base64 string for embedding in HTML
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_img_base64 = base64.b64encode(buffer.getvalue()).decode()

    context = {
        'order': order,
        'total': total,
        'qr_img_base64': qr_img_base64,
        'upi_id': upi_id,
        'payee_name': payee_name,
    }

    return render(request, 'catalog/payment_page.html', context)

@login_required
def place_order(request):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        cart = {}

    if cart:
        order = Order.objects.create(user=request.user)
        product_ids = [int(pid) for pid in cart.keys()]
        order.products.set(product_ids)
        order.save()
        request.session['cart'] = {}
        # Redirect to payment page with order id
        return redirect('payment_page', order_id=order.id)

    return redirect('product_list')
