from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from comments.forms import CommentForm
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
# Create your views here.


class IssueCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = models.Issue
    fields = ('title', 'type', 'status', 'details')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required
def issue_detail(request, pk):
    template_name = 'issues/issue_detail.html'
    issue = models.Issue.objects.get(pk=pk)
    comments = issue.comments.all()
    response_data = {}
    # Comment posted
    if request.is_ajax and request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.issue = issue
            new_comment.user = request.user
            # Save the comment to the database
            new_comment.save()
            response_data['content'] = new_comment.content
            response_data['user'] = serializers.serialize('json', [ new_comment.user, ])
            print("Created",new_comment.created)
            response_data['created'] = new_comment.created.strftime("%B %d, %Y, %I:%M %p")
            # ser_instance = serializers.serialize('json', [ new_comment, ])
            # return JsonResponse({"instance": ser_instance}, status=200)
            return JsonResponse(response_data)
        else: # Some form error
            return JsonResponse({"error": comment_form.errors}, status=400)
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
