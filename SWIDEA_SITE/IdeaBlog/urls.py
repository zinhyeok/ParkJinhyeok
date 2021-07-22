from django.urls import path
from . import views
appname = "ideaBlog"

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('create/', views.create_idea, name='create_idea'),
    path('<int:pk>/edit/', views.edit_idea, name='edit_idea'),
    path('<int:pk>/delete/', view=views.delete_idea, name='delete_idea'),
]
