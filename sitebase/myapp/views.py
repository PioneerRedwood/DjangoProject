from django.contrib.auth import authenticate, login, logout

from rest_framework import (
    viewsets, permissions, generics, filters,
    views
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import (
    BrandSerializer, PopulationSerializer, BrandSnapSerializer,
    AnalysisModelSerializer, HeadquarterSerializer, StoreAddressSerializer
)
from .models import (
    Brand, Headquarter, Population, AnalysisModel, StoreAddress,
    User,
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


class RegisterView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user=user)
            if user.is_authenticated:
                return Response(status=200)
        else:
            return Response(status=401)


class LogoutView(views.APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=200)


class BaseThemeView(generics.ListAPIView):
    """
    사용자로부터 테마 선택 입력받고 (1~5 레이블) AnalysisRatioModel 레이블 별 상위 10개 브랜드 반환
    """
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisModelSerializer

    def get_queryset(self):
        return self.queryset.order_by('average_sales_ratio', 'startup_cost_ratio',
                                      'rate_of_opening_ratio')

    def list(self, request, *args, **kwargs):
        # 여기에 request 값 읽어오기
        queryset = self.get_queryset().filter(label__iexact=2)
        query_result = list(queryset)

        top_brands = []
        for row in query_result:
            top_brands.append(
                [row.brand_name, float(row.average_sales_ratio + row.startup_cost_ratio + row.rate_of_opening_ratio)])
        top_brands.sort(key=lambda x: -x[1])
        brand_list = []
        for row in top_brands[:10]:
            brand_list.append(row[0])

        serializer = AnalysisModelSerializer(
            queryset.filter(brand_name__in=brand_list), many=True)
        return Response(serializer.data)


class CustomThemeView(generics.ListAPIView):
    """
    사용자가 특성의 우선순위를 입력 받아 그에 맞게 상위 10개 브랜드 반환
    """
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisModelSerializer

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        print(request.header.get('Authorization'))

        if request.user.is_authenticated:
            print(request.user, " : ", request.auth)
        else:
            print('로그인 안됨', request.user)

        analysis_data = self.get_queryset().filter(label__iexact=3)
        serializer = AnalysisModelSerializer(analysis_data, many=True)
        return Response(serializer.data)
