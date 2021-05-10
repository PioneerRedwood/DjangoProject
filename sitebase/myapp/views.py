from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.views import generic
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PopulationSerializer
from rest_framework import generics

from .models import Brand, Headquarter, Population, Account
from .forms import BrandSearchForm, RegistrationForm, AccountAuthenticationForm


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.filter(
            sector__lte='한식'
        ).order_by('brand_name')[:100]


# 브랜드 상세 페이지
# 로그인이 된 상태라면 모든 정보를 열람할 수 있도록 세션을 추가해야 함
class DetailView(generic.DetailView):
    model = Brand
    template_name = 'myapp/brand/detail.html'


class AddressView(generic.TemplateView):
    template_name = 'myapp/kakaomap.html'


class PopulationListView(generics.ListCreateAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer


# Form 을 이용한 검색 기능
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


# 인구수 rest framework 테스트
class PopulationView(viewsets.ModelViewSet):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 회원가입
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("myapp:index")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('myapp:index')
        else:
            context['form'] = form

    return render(request, 'myapp/register.html', context)


# 로그인
def login_view(request, *args, **kwargs):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("myapp:index")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("myapp:index")
    else:
        form = AccountAuthenticationForm()
        context['form'] = form

    return render(request, "myapp/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('myapp:index')


def get_redirect_if_exists(request):
    next_address = None
    if request.GET:
        if request.GET.get('next'):
            next_address = str(request.GET.get('next'))
    return next_address
