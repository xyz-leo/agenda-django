from django.shortcuts import get_object_or_404, render
from django.template.base import COMMENT_TAG_END
from contact.models import Contact
from django.http import Http404

# Create your views here.

def index(request):
    contacts = Contact.objects \
            .filter(show=True) \
            .order_by("first_name")[:10]

    context = {
            'contacts': contacts,
            }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
            'contact': single_contact
            }

    return render(request, 'contact/contact.html', context)
