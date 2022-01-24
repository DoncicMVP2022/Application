import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class ProjectFilter(django_filters.FilterSet):
    # finish_date = DateFilter(field_name="date_finish_task", lookup_expr='gte')

    class Meta:
        model = Projects
        fields = ['name', 'project_status', 'data_created']

