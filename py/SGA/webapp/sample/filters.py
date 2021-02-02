#!/usr/bin/env python

"""Custom filters for the Sample model, which work by selecting Sample objects
in the database based on meeting the desired criteria.

"""
import django_filters
from SGA.webapp.sample.models import Sample

class SampleFilter(django_filters.FilterSet):
    """Custom filter for the Sample model.  Filter options include greater
    than or equal to, and less than or equal to on the following 
    fields: ra, dec, sga_id, and diameter.

    The filter can be used in a form (see, e.g., list.html).

    """
    #field_name is the Sample object variable
    #lookup_expr is used to get ranges (currently using greater/less than or equal to  
    ra__gte = django_filters.NumberFilter(field_name='ra', lookup_expr='gte')
    ra__lte = django_filters.NumberFilter(field_name='ra', lookup_expr='lte')

    dec__gte = django_filters.NumberFilter(field_name='dec', lookup_expr='gte')
    dec__lte = django_filters.NumberFilter(field_name='dec', lookup_expr='lte')

    sgaid__gte = django_filters.NumberFilter(field_name='sga_id', lookup_expr='gte')
    sgaid__lte = django_filters.NumberFilter(field_name='sga_id', lookup_expr='lte')

    diam__gte = django_filters.NumberFilter(field_name='diam', lookup_expr='gte')
    diam__lte = django_filters.NumberFilter(field_name='diam', lookup_expr='lte')

    #ra__cone = django_filters.NumberFilter(field_name='ra', method='conesearch')

    # def conesearch(self, queryset, name, value):
    #     print('Conesearch!', name, value, self)
    #     return queryset
    #.filter(**{
    #        name: value,
    #    })
    
    class Meta:
        model = Sample
        #add variable to fields[] if looking for exact match
        fields = []

        def id(self):
            return self.sga_id
