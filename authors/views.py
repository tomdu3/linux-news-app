from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User


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


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {'user': user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        # TODO: Form submission control and validation - redirection to the profile page
        pass
    else:
        # TODO: Display the profile update form
        pass

    return render(request, 'update_profile.html', {'user': request.user})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        # TODO: Form deletion  control and validation - redirection to the profile page
        pass

    return render(request, 'delete_profile.html', {'user': request.user})