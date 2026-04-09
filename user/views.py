from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


def home(request):
    return render(request,'user/base.html')


def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now logged in.')
            return redirect('login')
    else:
        form=CustomUserCreationForm()    
    return render(request,'user/register.html',{'form':form})