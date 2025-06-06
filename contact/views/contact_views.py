from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.template.base import COMMENT_TAG_END
from contact.models import Contact

# Create your views here.

def contacts(request):
    contacts = Contact.objects \
            .filter(show=True) \
            .order_by("first_name")

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            }
    return render(request, 'contact/contacts.html', context)


def single_contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
            'contact': single_contact
            }

    return render(request, 'contact/single_contact.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:contacts')
    
    contacts = Contact.objects \
            .filter(show=True) \
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
