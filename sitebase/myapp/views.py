from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import FormView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PopulationSerializer
from rest_framework import generics

from .models import Brand, Headquarter, Population
from .forms import BrandSearchForm


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.filter(
            sector__lte='한식'
        ).order_by('brand_name')[:100]


class DetailView(generic.DetailView):
    model = Brand
    template_name = 'myapp/brand/detail.html'


class AddressView(generic.TemplateView):
    template_name = 'myapp/kakaomap.html'


class PopulationListView(generics.ListCreateAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer


# class PopulationDetail(generic.DetailView):
#     model = Population
#     template_name = 'myapp/'
# # 요청 url인 population에 대해서 urls.py에 정의된 view.Population_list 가 호출
# @api_view(['GET', 'POST'])
# def population_list(request, format=None):
#     if request.method == 'GET':
#         populations = Population.objects.all()
#         serializer = PopulationSerializer(populations, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PopulationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # 요청 url인 population/번호 에 대해 urls.py 에 정의된 view.population_detail 이 호출
# @api_view(['GET', 'PUT', 'DELETE'])
# def population_detail(request, pk, format=None):
#     try:
#         population = Population.objects.get(pk=pk)
#     except Population.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PopulationSerializer(population)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PopulationSerializer(population, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         population.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SearchFromView(FormView):
    form_class = BrandSearchForm
    template_name = 'myapp/brand/search.html'

    def form_valid(self, form):
        search_keyword = form.cleaned_data['search_keyword']
        brand_list = Brand.objects.filter(brand_name__contains=search_keyword)

        context = {
            'form': form,
            'search_term': search_keyword,
            'brand_list': brand_list,
        }

        return render(self.request, self.template_name, context)
