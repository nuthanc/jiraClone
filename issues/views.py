from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
# Create your views here.


class IssueCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = models.Issue
    fields = ('title', 'type', 'status', 'details')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class IssueDetail(generic.detail.DetailView):
    model = models.Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if context['issue'].type == "ST":
            context['className'] = "badge badge-success"
        elif context['issue'].type == "BU":
            context['className'] = "badge badge-danger"
        else:
            context['className'] = "badge badge-primary"

        return context

class IssueList(generic.list.ListView):
    # paginate_by = 2 For 2 issues per page.
    model = models.Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for issue in context['issue_list']:
            if issue.type == "ST":
                issue.className = "list-group-item-warning"
                issue.textColor = "text-success"
            elif issue.type == "BU":
                issue.className = "list-group-item-danger"
                issue.textColor = "text-danger"
            else:
                issue.className = "list-group-item-primary"
                issue.textColor = "text-primary"
        return context

class IssueUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = models.Issue
    fields = ('title', 'type', 'status', 'details')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class IssueDelete(generic.edit.DeleteView):
    model = models.Issue
    success_url = reverse_lazy('issues:list')
