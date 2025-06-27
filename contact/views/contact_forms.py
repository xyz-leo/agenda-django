from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from contact.forms import ContactForm 
from contact.models import Contact


@login_required
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        context = {
                'form': form,
                'form_action': form_action,
                'title': 'Create New Contact',
                'button': 'Create',
                }
        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact:details', contact_id=contact.pk)

        return render(request, 'contact/create.html', context)

    context = {
            'form': ContactForm(user=request.user),
            'form_action': form_action,
            'title': 'Create New Contact',
            'button': 'Create',
            }

    return render(request, 'contact/create.html', context)


@login_required
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, user=request.user)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact, user=request.user)
        context = {
                'form': form,
                'form_action': form_action,
                'title': 'Update Contact',
                'button': 'Update',
                }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:details', contact_id=contact.pk,)

        return render(request, 'contact/create.html', context)

    context = {
            'form': ContactForm(instance=contact, user=request.user),
            'form_action': form_action,
            'title': 'Update Contact',
            'button': 'Update',
            }

    return render(request, 'contact/create.html', context)


@login_required
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, user=request.user)
    contact.delete()
    return redirect('contact:contacts')
