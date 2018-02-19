from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _t
from utils.fields import MultilingualCharField
from utils.fields import MultilingualTextField


class Article(models.Model):
    class Meta:
        db_table = "articles"

    title = MultilingualCharField(_t('Title'), max_length=200,)
    text = MultilingualTextField(_t('Text'),blank=True,)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title
