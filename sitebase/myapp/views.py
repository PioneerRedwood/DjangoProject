from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.views import generic
from django.views.generic import FormView
from django.contrib.auth import authenticate, login

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PopulationSerializer
from rest_framework import generics

from .models import Brand, Headquarter, Population, Account
from .forms import BrandSearchForm


# 가장 처음에 보이는 페이지
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


from .forms import RegistrationForm, AccountAuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data.get('password'))
            # user.save()

            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_pass)
            # login(request, account)
            messages.success(request, '등록됐습니다.'.format(request.user.username))
            return redirect('myapp:index')
            # return HttpResponse(Account.objects.all())
        else:
            messages.error(request, '오류')
            context['form'] = form
    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'myapp/register.html', context)


def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("myapp:index")

    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(type(form), form.__str__)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In")
            return redirect("myapp:index")
        else:
            # messages.error(request, "please Correct Below Errors")
            form = AccountAuthenticationForm(request.POST)
            return render(request, "myapp/login.html", {'form': form})
    else:
        form = AccountAuthenticationForm()
        context['form'] = form
    return render(request, "myapp/login.html", context)

# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged Out")
#     return redirect("home")
