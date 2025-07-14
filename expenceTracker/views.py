from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import Transactions
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect!')
            return redirect('sign_in')
        
    return render(request, 'login.html')
    
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists!')
            return redirect('sign_up')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email address already exists!')
            return redirect('sign_up')
        if password != confirm_password:
            messages.error(request, 'Password does not match!')
            return redirect('sign_up')
        if len(password) < 5:
            messages.error(request, 'password should include more than five letters!')
            return redirect('sign_up')

        create_account = User.objects.create_user(username=username, email=email, password=password)
        create_account.save()
        return redirect('sign_in')
    
    return render(request, 'signup.html')
    

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def edit_transactions(request, id):
    error_handle = get_object_or_404(Transactions, id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        amount  = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description')

        error_handle.transaction = title
        error_handle.amount = amount
        error_handle.date = date
        error_handle.description = description

        error_handle.save()
        return redirect('home')
    return render(request, 'edit-transactions.html', {'edit_transaction':error_handle})

def add_transactions(request):
    if request.method == "POST":
        try:
            category =  request.POST['category']
            amount = request.POST['amount']
            date = request.POST['date']
            title = request.POST['title']
            new_transaction = Transactions(
                user = request.user,
                title = title,
                category = category,
                amount = amount,
                date = date
            )
            new_transaction.save()
            return redirect('home')
        except (ValueError, KeyError):
            messages.error(request, 'please enter valid date format')
            return redirect('home')
        
def delete_form(request, id):
    delete_item = Transactions.objects.get(id=id)
    delete_item.delete()
    return redirect('home')

@login_required(login_url='login')
def home_page(request):
    homepage = Transactions.objects.filter(user = request.user)
    return render(request, 'home-page.html', {'home':homepage})