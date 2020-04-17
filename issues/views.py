from django.shortcuts import render
from django.views import generic

from . import models
# Create your views here.

class IssueCreate(generic.edit.CreateView):
    model = models.Issue
    fields = '__all__'

class IssueDetail(generic.detail.DetailView):
    model = models.Issue

