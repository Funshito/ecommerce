from decimal import Decimal
from e_commerce_app.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart
        
    def add(self, product, qty):
        product_id = product.id
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
        self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = (item['price'] * item['qty'])
            yield item
      
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def get_total_price(self):
        sub_total = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
        whole_total = sub_total + Decimal(5000)
        return whole_total
    
    def delete(self, product):
        product_id = str(product)
    
        if product_id in self.cart:
            del self.cart[product_id]
            print(product_id)
            self.save()
            
    def update(self, product, qty):
        product_id = str(product)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
            
        self.save()
    
    def save(self):
        self.session.modified = True