from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
]