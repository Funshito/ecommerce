from django.urls import path
from e_commerce_app import views

app_name = "e-commerce-app"

urlpatterns = [
    path('', views.index, name="homepage"),
    path('about/', views.about, name="about"),
    path('blog-detail/<int:pk>', views.blog_detail, name="blog-detail"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('product/', views.product, name="product"),
    path('product-detail/<int:pk>', views.product_detail, name="product-detail"),
    path('shoping-cart/', views.shoping_cart, name="shoping-cart"),
    # path('get-product/', views.get_product, name='get-product'),
    path('search/slug:category_slug/', views.category_list, name='category_list'),
]