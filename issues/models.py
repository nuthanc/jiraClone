from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Issue(models.Model):
    user = models.ForeignKey(User, related_name='issues',on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=250)
    issue_no = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    details = models.TextField(blank=False)

    class TypeOfIssue(models.TextChoices):
        STORY = 'ST', _('Story')
        BUG = 'BU', _('Bug')
        TASK = 'TA', _('Task')

    class Status(models.TextChoices):
        OPEN = 'OP', _('Open')
        IN_PROGRESS = 'IN', _('In Progress')
        CLOSED = 'CL', _('Closed')

    type = models.CharField(
        max_length=2,
        choices=TypeOfIssue.choices,
        default=TypeOfIssue.BUG,
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPEN,
    )

    def get_absolute_url(self):
        return reverse('issues:detail', kwargs={'pk': self.pk})

    def __str__(self):
        returnString = f"#{self.issue_no} {self.title}"
        return returnString
