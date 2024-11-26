from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Contact, Category
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# from django.http import JsonResponse
# from django.core.serializers import serialize


# Create your views here.

    
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})
    


def index(request):
    # all_products = Product.objects.all()
    category = Category.objects.all()
    # latest_products = Product.objects.all().order_by("")
    filter_value = request.GET.get('filter', 'all')
    # load_more = request.Get.get('all')
        
    if filter_value == 'Women':
        products = Product.objects.filter(category=1)[:8]
    elif filter_value == 'Men':
        products = Product.objects.filter(category=3)[:8]
    elif filter_value == 'Bag':
        products = Product.objects.filter(category=2)[:8]
    elif filter_value == 'Shoes':
        products = Product.objects.filter(category=4)[:8]
    elif filter_value == 'Accessories':
        products = Product.objects.filter(category=5)[:8]
    # elif filter_value == 'all':
    #     products = Product.objects.filter(category='')[:12]
        # if load_more:
        #     products = Product.objects.all()[:12]
        #     return JsonResponse({'products': serialize('json', products)})
        # else:
        #     return JsonResponse({'products': serialize('json', products[:8])})
    else:
        products = Product.objects.all()[:8]
    context = {
       'products': products,
       'categories': category,
       'filter_value': filter_value
    }
        
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(name=name, email=email, subject=subject, message=message)
        email_subject = f'{subject}: FROM FUNSHO STORE WEBSITE'
        email_data = {
            'name': name,
            'email': email,
            'message': message
        }
        html_message = render_to_string('contact-mail.html', email_data)
        plain_message = strip_tags(html_message)
        from_email = email
        recepient_list = [settings.EMAIL_HOST_USER, ]
        try:
            email_message = EmailMessage(email_subject, plain_message, to=recepient_list, from_email=from_email)
            email_message.send()
            data.save()
            messages.success(request, 'Message sent successfully')
        except:
            messages.error(request, 'Failed to send message')
    return render(request, 'contact.html')

def product(request):
    category = Category.objects.all()
    
    # fetching product from server
    filter_value = request.GET.get('filter', 'all')
        
    if filter_value == 'Women':
        products = Product.objects.filter(category=1)[:12]
    elif filter_value == 'Men':
        products = Product.objects.filter(category=3)[:12]
    elif filter_value == 'Bag':
        products = Product.objects.filter(category=2)[:12]
    elif filter_value == 'Shoes':
        products = Product.objects.filter(category=4)[:12]
    elif filter_value == 'Accessories':
        products = Product.objects.filter(category=5)[:12]
    else:
        products = Product.objects.all()
    context = {
       'products': products,
       'categories': category,
       'filter_value': filter_value
    }
    return render(request, 'product.html', context)

def product_detail(request, pk):
    product_detail = get_object_or_404(Product, id = pk)
    context = {
        'details': product_detail
    }
    return render(request, 'product-detail.html', context)

def shoping_cart(request):
    
    # return JsonResponse(data)
    return render(request, 'shoping-cart.html')



# fetching product data 
# def get_product(request):
#     try:
#         product = serialize('json', Product.objects.all())
#         data = {
#             'product_list': product
#             # 'price': product.price,
#             # 'description': product.description
#             # 'id': product.id,
#             # 'image': product.image,
#         }
#         return JsonResponse(data)
#     except Product.DoesNotExist:
#         return JsonResponse({'error': 'Product not found'}, status=404)