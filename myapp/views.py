from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import AddTransactionForm,ProfileForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='login')
def index(request):
    try:
        profile_obj = Profile.objects.get(user=request.user)
        transaction_obj = Transaction.objects.filter(profile=profile_obj).order_by('-created_at')
        if request.method == 'POST':
            form = AddTransactionForm(request.POST)
            if form.is_valid():

                transaction_name =  form.cleaned_data['transaction_name']
                transaction_amount = form.cleaned_data['amount']
                transaction_type =  form.cleaned_data['transaction_type']
                if transaction_type == 'Positive':
                    profile_obj.balance += float(transaction_amount)
                else:
                    profile_obj.expense += float(transaction_amount)
                    profile_obj.balance -= float(transaction_amount)
                profile_obj.save()
                trans = form.save(commit=False)
                trans.profile = profile_obj
                trans.save()
                messages.success(request,"Transaction Added Successfully.")
                return redirect('/')
        else:
            form = AddTransactionForm()
        paginator = Paginator(transaction_obj, 4)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Exception as e:
        print(e)
    context = {
        'profile_obj':profile_obj,
        'transaction_obj':transaction_obj,
        'form':form,
        'page_obj':page_obj,
    }
    return render(request,'index.html',context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user_obj = User.objects.filter(username=email)

            if not user_obj.exists():
                messages.error(request, 'The email doesn''t exists.')
                return HttpResponseRedirect(request.path)
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully.')
                return redirect('/')
            messages.error(request, 'Invalid credential.')
            return HttpResponseRedirect(request.path)
        return render(request, 'login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']

            user_obj = User.objects.filter(username=email)

            if user_obj.exists():
                messages.error(
                    request, 'the email you provided was already registered.')
                return HttpResponseRedirect(request.path)

            register_obj = User.objects.create_user(
                username=email, email=email, first_name=first_name, last_name=last_name)
            register_obj.set_password(password)
            register_obj.save()
            user = authenticate(
                    username = email,
                    password = password,
                )
            if user is not None:
                login(request,user)
                messages.success(
                    request, f'Your account {email} has been registered.')
                return redirect('profile')
    return render(request, 'signup.html')



@login_required(login_url='login/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login/')
def user_profile(request):
    profile_obj = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Saved.")
            return redirect(request.path)
    else:
        form = ProfileForm(instance=profile_obj)
    context = {'form':form}
    return render(request,'user_profile.html',context)