from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')
app_name = 'shop'


urlpatterns = [
    path('achieve/<yyyy:year>/', views.achieve_year, name='achieve_year'),
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
]
