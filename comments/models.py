from django.db import models
from django.utils import timezone

from issues.models import Issue

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Comment(models.Model):
  content = models.TextField(blank=False)
  issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
  created = models.DateTimeField(editable=False)
  modified = models.DateTimeField()

  def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.content