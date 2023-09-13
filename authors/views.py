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
        if request.POST['form_type'] == 'registration':
            username = request.POST["username"]
            password = request.POST["password"]
            print(username, password)
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error logging into your account. Please check your username and password.'))
            return redirect('login')
    else:
        return render(request, 'authentication/signup.html', {})

