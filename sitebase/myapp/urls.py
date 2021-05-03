from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('brand/', views.IndexView.as_view(), name='index'),
    path('brand/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('address/', views.AddressView.as_view(), name='address'),
    path('population/', views.PopulationListView.as_view(), name='population_list'),
    path('brand/search/', views.SearchFromView.as_view(), name='brand_search'),
]
