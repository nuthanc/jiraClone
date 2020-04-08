from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.


class Issue(models.Model):
    
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

    details = models.TextField(blank=False)

    def get_absolute_url(self):
        return reverse('home')
