from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth import authenticate
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login as auth_login





# Create your views here.

def Information(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            object.set_password(password)
            object.save()
            profile = Employee()
            profile.user = object
            profile.save()
            messages.success(request, 'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active and user.is_superuser:
                auth_login(request, user)
                if request.GET.get('next', None):
                    return redirect(request.GET.get['next'])
                return redirect('dash')
            else:
                if user.is_active:
                    auth_login(request, user)
                return redirect('work')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def dasboard_view(request):
    # employee = Employee.objects.get(id=id)
    return render(request, 'dashboard.html')

def worksite_view(request):
    # employee = Employee.objects.get(user_id=request.user.id)
    return render(request, 'worksite-detail.html')
