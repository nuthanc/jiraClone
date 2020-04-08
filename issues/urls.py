from django.urls import path
from . import views

app_name = 'issues'

urlpatterns = [
    path('new/', views.IssueCreate.as_view(), name='create'),
]
