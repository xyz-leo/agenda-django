from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()
    button = 'Create'
    title = 'Register'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User successfully created!")
            return redirect('contact:home')
            # redirect pra pagina de view de usuario

    return render(request, 'contact/create.html', {'form': form, 'title': title, 'button': button})
