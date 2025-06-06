from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.template.base import COMMENT_TAG_END
from contact.models import Contact


def create(request):
    context = {
            'contact': 'a'
            }

    return render(request, 'contact/create.html', context)

