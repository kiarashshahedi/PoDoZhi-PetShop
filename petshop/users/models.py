from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='شماره تلفن')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')
    

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255, verbose_name='آدرس ۱')
    address_line2 = models.CharField(max_length=255, blank=True, verbose_name='آدرس ۲')
    city = models.CharField(max_length=100, verbose_name='شهر')
    state = models.CharField(max_length=100, verbose_name='استان')
    postal_code = models.CharField(max_length=20, verbose_name='کد پستی')
    country = models.CharField(max_length=100, verbose_name='کشور')

    def __str__(self):
        return f'{self.address_line1}, {self.city}'

class OrderHistory(models.Model):
    user = models.ForeignKey(User, related_name='order_history', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مبلغ کل')

    def __str__(self):
        return f'Order {self.id} - {self.user.username}'
