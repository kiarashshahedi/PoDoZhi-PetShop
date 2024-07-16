from django import forms
from .models import Product, ProductImage

# adding products in website page (out of admin pannel)
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'category', 'name', 'description', 'price', 'stock', 'available', 
#             'weight', 'dimensions', 'manufacturer', 'warranty', 'color', 
#             'breed', 'life_stage', 'flavor', 'nutritional_info', 'recommended_usage',
#             'expire_date', 'origin_country', 'tags', 'is_featured', 'featured_price'
#         ]
# adding images of products in website page (out of admin pannel)
# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
