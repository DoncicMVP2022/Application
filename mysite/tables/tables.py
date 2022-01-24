import django_tables2 as tables
from .models import Task


class MyTableTask(tables.Table):
    class Meta:
        model = Task
        fields = {'condition', 'date_finish_task'}
