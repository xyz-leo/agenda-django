from django.contrib import messages
from django.contrib.auth.views import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from contact.models import Contact


@login_required
def contacts(request):
    contacts = Contact.objects \
            .filter(user=request.user, show=True) \
            .order_by("first_name")

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            }
    return render(request, 'contact/contacts.html', context)

@login_required
def single_contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True, user=request.user)

    context = {
            'contact': single_contact
            }

    return render(request, 'contact/single_contact.html', context)

@login_required
def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:contacts')
    
    contacts = Contact.objects \
            .filter(show=True, user=request.user) \
            .filter(
                    Q(first_name__icontains=search_value) |
                    Q(last_name__icontains=search_value) |
                    Q(phone__icontains=search_value) |
                    Q(email__icontains=search_value)
            )\
            .order_by('-id')

    paginator = Paginator(contacts, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            }
    return render(request, 'contact/contacts.html', context)
