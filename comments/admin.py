from django.contrib import admin
from comments.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
  list_display = ('user', 'content', 'user', 'created', 'modified')
  list_filter = ['created']
  search_fields = ['content', 'user']

admin.site.register(Comment, CommentAdmin)