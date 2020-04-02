from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Issues(models.Model):

    class TypeOfIssue(models.TextChoices):
        STORY = 'ST', _('Story')
        BUG = 'BU', _('Bug')
        TASK = 'TA', _('Task')

    class Status(models.TextChoices):
        OPEN = 'OP', _('Open')
        IN_PROGRESS = 'IN', _('In Progress')
        CLOSED = 'CL', _('Closed')

    type_of_issue = models.CharField(
        max_length=2,
        choices=TypeOfIssue.choices,
        default=TypeOfIssue.BUG,
    )

    status = models.CharField(
        max_length=2,
        choices=TypeOfIssue.choices,
        default=TypeOfIssue.BUG,
    )

