from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name = "list"),
    path('<slug:slug>', views.post_page, name = "page"),
]