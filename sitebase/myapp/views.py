from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Brand, Headquarter


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.filter(
            sector__lte='한식'
        ).order_by('brand_name')[:100]


class DetailView(generic.DetailView):
    model = Brand
    template_name = 'myapp/detail.html'
