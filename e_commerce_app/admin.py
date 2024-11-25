from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
        
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'in_stock']
    list_filter = ['in_stock', 'is_active']
    prepopulated_fields = {'slug': ('name', )}
    
    
# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title', )}
    


# admin.site.register(Order)

# admin.site.register(Review)

