from django.contrib.auth.views import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm


@login_required
def user_view(request):
    return render(request, 'contact/login.html')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User successfully created!")
            return redirect('contact:login_view')

    return render(request, 'contact/create.html', {'form': form, 'title': 'Register', 'button': 'Register'})


def login_view(request):
    form = AuthenticationForm(request)
    if request.user.is_authenticated:
        return redirect('contact:user_view')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Login succesful!")
            return redirect('contact:home')
        messages.error(request, "Invalid login")

    return render(request, 'contact/login.html', {'form': form, 'title': 'Login', 'button': 'Sign in'})


@login_required
def logout_view(request):
    auth.logout(request)
    messages.success(request, "Logout succesful!")
    return redirect('contact:login_view')


@login_required
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(request, 'contact/create.html', {'form': form, 'button': 'Send', 'title': 'Update User Information'})
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, 'contact/create.html', {'form': form, 'button': 'Send', 'title': 'Update User Information'})

    form.save()
    messages.success(request, 'Your profile was updated successfully.')
    return redirect('contact:user_view')
