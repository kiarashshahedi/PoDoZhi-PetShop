from django.db import models
from django.contrib.auth.models import AbstractUser
from .myusermanager import MyUserManager
from django.db.models.signals import post_save
import datetime
from django.contrib.auth.models import User



class MyUser(AbstractUser):
    user = models.OneToOneField('self', on_delete=models.CASCADE, unique=True, related_name='MyUser', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)    
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)
    is_premium_member = models.BooleanField(default=False)
    mobile = models.CharField(max_length=11, unique=True)
    otp = models.IntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    backend = 'custom_loggin.mybackend.ModelBackend'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def get_age(self):
        if self.date_of_birth:
            today = datetime.date.today()
            birth_date = self.date_of_birth
            age = today.year - birth_date.year 
            return age
        
    def get_full_address(self):
        return self.address

    def __str__(self):
        return self.mobile


# Create a user Profile by default when user signs up

# Update the create_profile function to perform actions after MyUser instance creation
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Perform actions after MyUser instance creation here
        pass

# Connect the signal to the function
post_save.connect(create_profile, sender=MyUser)





class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='شماره تلفن')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')
    

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(MyUser, related_name='addresses', on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255, verbose_name='آدرس ۱')
    address_line2 = models.CharField(max_length=255, blank=True, verbose_name='آدرس ۲')
    city = models.CharField(max_length=100, verbose_name='شهر')
    state = models.CharField(max_length=100, verbose_name='استان')
    postal_code = models.CharField(max_length=20, verbose_name='کد پستی')
    country = models.CharField(max_length=100, verbose_name='کشور')

    def __str__(self):
        return f'{self.address_line1}, {self.city}'

class OrderHistory(models.Model):
    user = models.ForeignKey(MyUser, related_name='order_history', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مبلغ کل')

    def __str__(self):
        return f'Order {self.id} - {self.user.username}'
