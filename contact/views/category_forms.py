from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from contact.forms import CategoryForm
from contact.models import Contact, Category

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)

    return render(request, 'contact/contacts_by_category.html', {
        'categories': categories
    })

@login_required
def category_create(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('contact:category_list')

    return render(request, 'contact/create.html', {
        'form': form,
        'title': 'Create Category',
        'button': 'Create'
    })

@login_required
def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id, user=request.user)

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('contact:category_list')

    return render(request, 'contact/create.html', {
        'form': form,
        'title': 'Edit Category',
        'button': 'Update'
    })


@login_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id, user=request.user)

    if request.method == 'POST':
        category.delete()
        return redirect('contact:category_list')

    return render(request, 'contact/create.html', {'category': category})


@login_required
def contacts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id, user=request.user)
    contacts = Contact.objects.filter(category=category, user=request.user, show=True)

    return render(request, 'contact/category_contacts.html', {
        'contacts': contacts,
        'category': category
    })


@login_required
def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id, user=request.user)

    return render(request, 'contact/category_detail.html', {
        'category': category
    })
