from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, AddressForm
from .models import Address, OrderHistory

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'users/profile.html', {'user_form': user_form})

@login_required
def manage_addresses(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('manage_addresses')
    else:
        form = AddressForm()
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'users/manage_addresses.html', {'form': form, 'addresses': addresses})

@login_required
def order_history(request):
    orders = OrderHistory.objects.filter(user=request.user)
    return render(request, 'users/order_history.html', {'orders': orders})
