from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email =  models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
    def __str__(self):
        return self.subject
    
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/uploads/')
    objects = models.Manager()
    products = ProductManager()
    
    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='blog/uploads/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)
        
    def __str__(self):
        return self.title
        
     
    
# class Shoe(Product):
#     size = models.CharField(max_length=10)
#     color = models.CharField(max_length=50)

# class Cloth(Product):
#     size = models.CharField(max_length=10)
#     material = models.CharField(max_length=100)

# class Bag(Product):
#     material = models.CharField(max_length=100)
#     style = models.CharField(max_length=50)

# class Accessory(Product):
#     accessory_type = models.CharField(max_length=100)
    
    
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Order #{self.id} by {self.user.username}'    
    

        
# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Ratings from 1 to 5
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username} review for {self.product.name}'