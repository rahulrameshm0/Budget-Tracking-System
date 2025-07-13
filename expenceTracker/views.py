from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import Transactions
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def sign_in(request):
    uesername = request.POST.get('username')
    password = request.POST.get('passsword')

    user = authenticate(uesername=uesername,password=password)
    if user is not None:
        login(request, user)
        messages.error(request, 'username or password is incorrect!')
        return redirect('home')
    
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
            messages.error(request, 'password should include atleast 4 charctors')
            return redirect('sign_up')

        create_account = User.objects.create_user(username=username, email=email, password=password)
        create_account.save()
        return redirect('sign_in')
    
    return render(request, 'signup.html')
    

def sign_out(request):
    login(request)
    return redirect('sign_in')

def edit_transactions(request, id):
    error_handle = get_object_or_404(Transactions, id=id)
    if request.method == "POST":
        transactions = request.POST.get('transactions')
        amount  = request.POST.get('amount')
        date = request.POST.get('date')

        error_handle.transaction = transactions
        error_handle.amount = amount
        error_handle.date = date

        error_handle.save()
        return redirect('home')
    return render(request, 'edit.transaction.html', {'edit-transaction':error_handle})