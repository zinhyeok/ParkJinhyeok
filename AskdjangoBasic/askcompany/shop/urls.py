from django.urls import path
from django.urls.resolvers import URLPattern

app_name = 'shop'

urlpatterns = [
    # path('item/',item_list,name="item_list") -> item/주소, item_list 함수 호출, url(?) 이름은 "item_list"
    path('achieve/<yyyy:year>/', views.achieve_year),
    path('', views.item_list),
]
