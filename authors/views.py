from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        # Login In Code
        if request.POST['form_type'] == 'login':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            message = 'You are logged in. Congrats!'
        elif request.POST['form_type'] == 'registration':
            username = request.POST["username"]
            password = request.POST["password"]
            message = 'You are now registered! Congrats!'

            user = authenticate(request, username='admin', password='admin')
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, message, extra_tags='success')
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, ('Login error! Please check your username and password.'), extra_tags='danger')
            return redirect('login')
    else:
        return render(request, 'authentication/signup.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!', ), extra_tags='info')
    return redirect('/')
