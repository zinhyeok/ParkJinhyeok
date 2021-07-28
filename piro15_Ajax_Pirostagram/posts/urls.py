from django.urls import path
from . import views
import posts

app_name = posts

urlpatterns = [path("", view=views.post_main, name="post_main")]
