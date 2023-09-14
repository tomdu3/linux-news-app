from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.


def login_user(request):
    message = ''
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ('You are logged in. Congrats!'), extra_tags='success')
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, ('Login error! Please check your username and password.'), extra_tags='danger')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!', ), extra_tags='info')
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered!'), extra_tags='success')
            return redirect('/')
    else:
        form = SignUpForm()

    context = {'form': form} 
    return render(request, 'authentication/signup.html', context)