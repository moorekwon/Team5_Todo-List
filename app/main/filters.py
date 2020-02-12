import django_filters

from main.models import Todo


class SearchFilter(django_filters.FilterSet):
    Model = Todo
    fields = ['text', ]
