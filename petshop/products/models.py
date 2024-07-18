from django.db import models
from petshop import settings
import datetime
from users.models import MyUser

# animal type 
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#category of products
class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    animal_type = models.ForeignKey(Type, related_name='main_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

        
# SubCategories
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(MainCategory, related_name='sub_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    
# product class         
class Product(models.Model):
    
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='نام')
    name_in_list = models.CharField(max_length=255, verbose_name=' نام داخل لیست', default='name')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')
    stock = models.PositiveIntegerField(verbose_name='موجودی') 
    available = models.BooleanField(default=True, verbose_name='موجود است/نیست') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی') 
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='وزن بر اساس کیلوگرم')
    dimensions = models.CharField(max_length=100, blank=True, verbose_name='ابعاد به صورت متنی')
    manufacturer = models.CharField(max_length=255, blank=True, verbose_name='اسم سازنده (برند)')
    warranty = models.CharField(max_length=255, blank=True, verbose_name='اطلاعات گارانتی')
    color = models.CharField(max_length=50, blank=True, verbose_name='رنگ محصول')
    breed = models.CharField(max_length=50, blank=True, verbose_name='نژاد') 
    life_stage = models.CharField(max_length=50, blank=True, verbose_name='مرحله زندگی مناسب (سن)')
    flavor = models.CharField(max_length=50, blank=True, verbose_name='طعم دهنده ') 
    nutritional_info = models.TextField(blank=True, verbose_name='اطلاعات تغذیه ای')
    recommended_usage = models.TextField(blank=True, verbose_name='دستورالعمل استفاده توصیه شده') 
    expire_date = models.DateField(null=True, blank=True, verbose_name='تاریخ انقضا')
    origin_country = models.CharField(max_length=100, blank=True, verbose_name='کشور سازنده')  
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='برچسب ها برای جستجو و فیلتر')
    is_featured = models.BooleanField(default=False, verbose_name='تخفیف')
    featured_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='قیمت تخفیف خورده')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    
    
# product images 
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='تصویر')

    def __str__(self):
        return f'{self.product.name} Image'
    
    
# tags model 
class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')

    def __str__(self):
        return self.name
    
    
#the rate of the product
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)  # Rating (1 to 5 stars)
    comment = models.TextField(null=True, blank=True)  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = []


    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"

#Customers Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='customer_orders', related_query_name='customer_order')  # Add related_name and related_query_name
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    