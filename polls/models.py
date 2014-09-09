import os

from django.db import models
from uuidfield.fields import UUIDField
from django.utils.text import slugify


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


def upload_document(instance, filename):
    filename = os.path.splitext(filename)
    filename = (slugify(unicode(" ".join(filename[:-1]))) + filename[-1]).lower()

    return u'{}/{}'.format(
                "logos", filename,
            )


class Question(CommonInfo):
    name = models.CharField(max_length=255)
    uuid = UUIDField(auto=True)
    docfile = models.FileField(upload_to=upload_document, blank=True, null=True)
    counter = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Choice(CommonInfo):
    question = models.ForeignKey(Question)
    user_agent = models.TextField(blank=True)

    def __unicode__(self):
        return self.question.name

