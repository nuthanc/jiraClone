from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from comments.forms import CommentForm
# Create your views here.


class IssueCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = models.Issue
    fields = ('title', 'type', 'status', 'details')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def issue_detail(request, pk):
    template_name = 'issues/issue_detail.html'
    issue = models.Issue.objects.get(pk=pk)
    comments = issue.comments.all()
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.issue = issue
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    data = {
        'issue': issue,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, template_name, data)

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
