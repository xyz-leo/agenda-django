from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
            'a': 'a',
            }
    return render(request, 'contact/home.html', context)

