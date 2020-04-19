from django.urls import path, re_path
from . import views

app_name = 'issues'

urlpatterns = [
    path('', views.IssueList.as_view(), name='list'),
    path('new/', views.IssueCreate.as_view(), name='create'),
    re_path('(?P<pk>\d+)/', views.IssueDetail.as_view(), name='detail'),
]
