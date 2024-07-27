import django_filters
from teequeapp.models import Service

class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = {
            'price': ['lt', 'gt'],
            'category_id': ['exact'],
        }

    # filter by seller country and
    # filter by service ratings + seller rating 
    # filter by seller availability 
