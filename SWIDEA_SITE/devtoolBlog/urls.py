from django.urls import path
from . import views

app_name = 'devtoolBlog'

urlpatterns = [
    path('', views.devtool_list, name='devtool_list'),
    path('<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('create/', views.create_devtool, name='create_devtool'),
    path('<int:pk>/edit/', views.edit_devtool, name='edit_devtool'),
    path('<int:pk>/delete/', view=views.delete_devtool, name='delete_devtool'),
]
