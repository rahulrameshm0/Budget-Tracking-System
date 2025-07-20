from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import Transactions
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from decimal import Decimal
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
        txn_type = request.POST.get('type')
        amount_str = request.POST.get('amount')


        try:
            amount = Decimal(amount_str)
        except:
            messages.error(request, 'Please enter a valid amount.')
            return redirect('home')
        
        if txn_type == 'Expense':
            transactions = Transactions.objects.filter(user=request.user)
            total_income = sum(t.amount for t in transactions if t.type == 'Income')
            total_expense = sum(t.amount for t in transactions if t.type == 'Expense')
            current_balance = total_income - total_expense

            if amount > current_balance:
                messages.error(request, "You don't have enough money for this expense!")
                return redirect('home')

        try:
            category =  request.POST['category']
            amount = float(request.POST['amount'])
            date = request.POST['date']
            title = request.POST['title']
            txn_type = request.POST['type']
            new_transaction = Transactions(
                user = request.user,
                title = title,
                category = category,
                amount = amount,
                date = date,
                type=txn_type 
            )
            new_transaction.save()
            messages.success(request, f"{txn_type} added successfully!")
            return redirect('home')
        except (ValueError, KeyError):
            messages.error(request, 'please enter valid date format')
            return redirect('home')
        
def delete_form(request, id):
    delete_item = Transactions.objects.get(id=id)
    delete_item.delete()
    messages.success(request, 'Item deleted succesfully')
    return redirect('home')

@login_required(login_url='login')
def home_page(request):
    all_transaction = Transactions.objects.filter(user=request.user)

    total_income = sum(t.amount for t in all_transaction if t.type == "Income")
    total_expense = sum(t.amount for t in all_transaction if t.type == "Expense")
    balance = total_income - total_expense

    return render(request, 'home-page.html', {
        'transactions':all_transaction,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
    })

@login_required(login_url='login')
def filter_items(request):
    category = request.GET.get('all_category')
    date_filter = request.GET.get('all_month')
    transactions = Transactions.objects.filter(user=request.user)

    if category and category != 'All Category':
        transactions = Transactions.objects.filter(category=category, user=request.user)    

    if date_filter == 'All Dates':
        today = now()
        transactions = Transactions.objects.filter(date__month = today.month, date__year = today.year)

    elif date_filter == 'This Month':
        today = now()
        transactions = Transactions.objects.filter(date__month = today.month, date__year=today.year)

    elif date_filter == 'Last 3 Months':
        three_months_ago = now() - relativedelta(months=3)
        transactions = Transactions.objects.filter(date__gte = three_months_ago)

    elif date_filter == 'This Year':
        this_year = now().year
        transactions = Transactions.objects.filter(date__year = this_year)

    elif date_filter == 'Last Month':
        last_month = now() - relativedelta(months=1)
        transactions = Transactions.objects.filter(date__month = last_month.month, date__year = last_month.year)
    else:
        messages.error(request, "There is no transactions")

    return render(request, 'home-page.html', {'transactions':transactions})