from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Subject(models.Model):
    """
    Subject model representing subject from University schedule
    """
    name = models.CharField(max_length=100)
    group = models.ForeignKey('StudentGroup', related_name='subjects', null=True)


class Institute(models.Model):
    """
    Institute model representing Institute parsed from University
    """
    name = models.CharField(max_length=4)
    site_id = models.CharField(max_length=2, null=True)


class StudentGroup(models.Model):
    """
    Group representing students group in University
    """
    user = models.ForeignKey(User, related_name='student_groups', null=True)
    institute = models.ForeignKey(Institute, related_name='groups', null=True)
    name = models.CharField(max_length=15)
    site_id = models.CharField(max_length=4, null=True)

    @property
    def students_count(self):
        return self.user.all().count()


class Rate(models.Model):
    """
    Rate model representing rating of Student
    """
    user = models.ForeignKey(User, related_name='rate')
    value = models.FloatField()


class Table(models.Model):
    """
    Table model representing rate table
    """
    user = models.ForeignKey(User, related_name='table', default=1)
    name = models.CharField(max_length=200)


class TableRow(models.Model):
    """
    TableRow model representing each row in rate table
    """
    table = models.ForeignKey(Table, related_name='table_row')
    name = models.CharField(max_length=100, null=True)
    point = models.FloatField(default=0.0)
    coefficient = models.FloatField(default=1.0)
