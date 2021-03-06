from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from comments.forms import CommentForm
from comments.models import Comment
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

def ajax_comment_json_response(request, issue):
    response_data = {}
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
        response_data['id'] = new_comment.id
        response_data['created'] = new_comment.created.strftime("%B %d, %Y, %I:%M %p")
        return JsonResponse(response_data)
    else: # Some form error
        return JsonResponse({"error": comment_form.errors}, status=400)

def ajax_comment_delete(request):
    deleteData = request.body.decode("utf-8")
    if('=' in deleteData):
        comment_id = deleteData.split('=')[1]
    comment = Comment.objects.get(id=comment_id)
    if request.user.username == comment.user.username:
        comment.delete()
        return JsonResponse({})
    else:
        response = JsonResponse({"error": "Unauthorized"})
        response.status_code = 401
        return response

def ajax_comment_edit(request):
    pass
    
@login_required
def issue_detail(request, pk):
    template_name = 'issues/issue_detail.html'
    issue = models.Issue.objects.get(pk=pk)
    comments = issue.comments.all()
    # Comment posted or deleted
    if request.is_ajax and request.method == 'POST':
        return ajax_comment_json_response(request, issue)
    elif request.is_ajax and request.method == 'DELETE':
        return ajax_comment_delete(request)
    elif request.is_ajax and request.method == 'PUT':
        return ajax_comment_edit(request)
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
