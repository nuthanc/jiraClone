from django.contrib import admin
from issues.models import Issue

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
  fields = ['issue_no', 'title', 'type', 'status', 'details']
  readonly_fields = ('issue_no',)

  search_fields = ['issue_no', 'details']
  list_filter = ['type', 'status']


admin.site.register(Issue, IssueAdmin)
