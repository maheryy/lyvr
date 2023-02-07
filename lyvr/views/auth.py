from django.shortcuts import render, redirect
from django.contrib.auth import login
from lyvr.forms import RegisterForm, RegisterProForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, initial={'is_customer': True})
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def register_pro(request):
    if request.method == 'POST':
        form = RegisterProForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_pro = True
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterProForm()
    return render(request, 'registration/register_pro.html', {'form': form})