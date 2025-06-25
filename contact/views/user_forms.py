from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User successfully created!")
            return redirect('contact:login_view')
            # redirect pra pagina de view de usuario

    return render(request, 'contact/create.html', {'form': form, 'title': 'Register', 'button': 'Create'})

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Login succesful!")
            return redirect('contact:home')
        messages.error(request, "Invalid login")

    return render(request, 'contact/login.html', {'form': form, 'title': 'Login', 'button': 'Sign in'})

def logout_view(request):
    auth.logout(request)
    messages.success(request, "Logout succesful!")
    return redirect('contact:login_view')
