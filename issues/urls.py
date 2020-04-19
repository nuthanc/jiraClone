from django.urls import path
from . import views

app_name = 'issues'

urlpatterns = [
    path('', views.IssueList.as_view(), name='list'),
    path('new/', views.IssueCreate.as_view(), name='create'),
    path('<int:pk>/', views.IssueDetail.as_view(), name='detail'),
    path('edit/<int:pk>/', views.IssueUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', views.IssueDelete.as_view(), name='delete'),
]
