from django.urls import path, include

from . import views

app_name = 'myapp'

population_list = views.PopulationView.as_view({
    'post': 'create',
    'get': 'list'
})

population_detail = views.PopulationView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'detail': 'destroy'
})

urlpatterns = [
    path('brand/', views.IndexView.as_view(), name='index'),
    path('brand/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('address/', views.AddressView.as_view(), name='address'),
    path('brand/search/', views.SearchFromView.as_view(), name='brand_search'),

    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('population/', population_list, name='population_list'),
    path('population/<int:pk>/', population_detail, name='population_detail'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]