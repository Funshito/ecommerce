from django.shortcuts import render, get_object_or_404
from e_commerce_app.models import Product
from .cart import Cart
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)    
    return render(request, 'shoping-cart.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))        
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        cart_qty = cart.__len__()
        response = JsonResponse({'qty':cart_qty})
        return response
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cartqty = cart.__len__()
        carttotal = cart.get_subtotal_price()
        cart_whole_total = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal, 'total': cart_whole_total})
        return response
    
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))       
        cart.update(product=product_id, qty=product_qty)
        cartqty = cart.__len__()
        carttotal = cart.get_subtotal_price()
        cart_whole_total = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal, 'total': cart_whole_total})
        return response