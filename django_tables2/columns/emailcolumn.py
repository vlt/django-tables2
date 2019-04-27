# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.db import models

from django_tables2.utils import ucfirst

from .base import library
from .linkcolumn import BaseLinkColumn


@library.register
class EmailColumn(BaseLinkColumn):
    """
    Render email addresses to `mailto:`-links.

    Arguments:
        attrs (dict): HTML attributes that are added to the rendered
                      ``<a href="...">...</a>`` tag.
        text: Either static text, or a callable. If set, this will be used to
              render the text inside link instead of the value.

    Example::

        # models.py
        class Person(models.Model):
            name = models.CharField(max_length=200)
            email =  models.EmailField()

        # tables.py
        class PeopleTable(tables.Table):
            name = tables.Column()
            email = tables.EmailColumn()

        # result
        # [...]<a href="mailto:email@example.com">email@example.com</a>
    """

    def get_url(self, value):
        return "mailto:{}".format(value)

    @classmethod
    def from_field(cls, field):
        if isinstance(field, models.EmailField):
            return cls(verbose_name=ucfirst(field.verbose_name))
