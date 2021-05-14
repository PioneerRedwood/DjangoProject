from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets, permissions, generics, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    BrandSerializer, PopulationSerializer, BrandSnapSerializer,
    AnalysisModelSerializer, HeadquarterSerializer, RegisterSerializer, LoginSerializer,
    StoreAddressSerializer
)
from .models import (
    Brand, Headquarter, Population, Account, AnalysisModel, StoreAddress
)
from .forms import (
    RegistrationForm, AccountAuthenticationForm
)


class BrandListView(generics.ListAPIView):
    """
        브랜드 리스트 조회
    """
    search_fields = ['brand_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Brand.objects.all()
    serializer_class = BrandSnapSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('name'):
            queryset = self.get_queryset().filter(brand_name__contains=request.GET.get('name'))
        elif request.GET.get('id'):
            queryset = self.get_queryset().filter(id__iexact=request.GET.get('id'))
        else:
            queryset = self.get_queryset()

        serializer = BrandSnapSerializer(queryset, many=True)
        return Response(serializer.data)


class BrandDetailView(generics.ListAPIView):
    """
        브랜드 상세 정보
    """
    search_fields = ['brand_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('name'):
            queryset = self.get_queryset().filter(brand_name__iexact=request.GET.get('name'))

        else:
            queryset = self.get_queryset()

        serializer = BrandSerializer(queryset)
        return Response(serializer.data)


class HeadquarterView(generics.ListAPIView):
    """
        본사 리스트 조회
    """
    queryset = Headquarter.objects.all()
    serializer_class = HeadquarterSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('mutual'):
            queryset = self.get_queryset().filter(mutual__contains=request.GET.get('mutual'))
        else:
            queryset = self.get_queryset()
        serializer = HeadquarterSerializer(queryset, many=True)
        return Response(serializer.data)


class StoreAddressView(generics.ListAPIView):
    """
        가게 위치 정보 조회
    """
    queryset = StoreAddress.objects.all()
    serializer_class = StoreAddressSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('do') and request.GET.get('sigu') and request.GET.get('dong') and request.GET.get('sector'):
            queryset = self.get_queryset().filter(
                do__iexact=request.GET.get('do'),
                sigu__iexact=request.GET.get('sigu'),
                dong__iexact=request.GET.get('dong'),
                sector__iexact=request.GET.get('sector'),
            )
        else:
            queryset = self.get_queryset()
        serializer = StoreAddressSerializer(queryset, many=True)
        return Response(serializer.data)


class PopulationListView(generics.ListAPIView):
    """
        인구수 정보 조회
    """
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('do') and request.GET.get('sigu') and request.GET.get('dong'):
            queryset = self.get_queryset().filter(
                do__iexact=request.GET.get('do'),
                sigu__iexact=request.GET.get('sigu'),
                dong__iexact=request.GET.get('dong'))
        else:
            queryset = self.get_queryset()
        serializer = PopulationSerializer(queryset, many=True)
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permissions_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# 사용 안함
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("myapp:index")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            # account = authenticate(username=username, password=raw_password)
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            # API에 맞는 Response를 보내야 함
            if destination:
                return redirect(destination)
            return redirect('myapp:index')
        else:
            context['form'] = form

    return render(request, 'myapp/register.html', context)


class LoginView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


# 로그인
def login(request, *args, **kwargs):
    context = {}
    user = request.user

    # if user.is_authenticated:
    #     return redirect("myapp:index")

    if request.method == 'POST':
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
                return render(request, "myapp/login.html", context)
        return HttpResponse(status=200)
    else:
        form = AccountAuthenticationForm()
        context['form'] = form
        return render(request, "myapp/login.html", context)

    # return render(request, "myapp/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('myapp:index')


def get_redirect_if_exists(request):
    next_address = None
    if request.GET:
        if request.GET.get('next'):
            next_address = str(request.GET.get('next'))
    return next_address


class BaseThemeView(generics.ListAPIView):
    """
    사용자로부터 테마 선택 입력받고 (1~5 레이블) AnalysisRatioModel 데이터 추출
    리스트 형태로 만든 뒤 정렬하고 순위에 맞는 상위 10개 브랜드 반환
    """
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisModelSerializer

    def get_queryset(self):
        return self.queryset.order_by('average_sales_ratio', 'startup_cost_ratio',
                                      'rate_of_opening_ratio')

    def list(self, request, *args, **kwargs):
        # 여기에 request 값 읽어오기
        queryset = self.get_queryset().filter(label__iexact=2)
        print(queryset)
        query_result = list(queryset)

        top_brands = []
        for row in query_result:
            top_brands.append(
                [row.brand_name, float(row.average_sales_ratio + row.startup_cost_ratio + row.rate_of_opening_ratio)])
        top_brands.sort(key=lambda x: -x[1])
        brand_list = []
        for row in top_brands[:10]:
            brand_list.append(row[0])
        print(brand_list)

        serializer = AnalysisModelSerializer(
            # AnalysisModel.objects.filter(brand_name__in=brand_list).filter(label__iexact=2), many=True)
            queryset.filter(brand_name__in=brand_list), many=True)
        return Response(serializer.data)


class CustomThemeView(generics.ListAPIView):
    """
    사용자가 특성의 우선순위를 입력 받아 그에 맞게 상위 10개 브랜드 반환
    분석 모델 자체와 정규화된 분석 모델 리스트 조인해서 보내야함
    join > AnalysisModel + AnalysisRatioModel
    """
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisModelSerializer

    def get_queryset(self):
        return self.queryset.filter
