import django_filters
from allstars.forms import SearchForm
from allstars.models import *


class PersonRecordFilter(django_filters.FilterSet):
	first_name = django_filters.CharFilter(
		field_name='first_name',
		label='First Name',
		lookup_expr='icontains'
	)

	last_name = django_filters.CharFilter(
		field_name='last_name',
		label='Last Name',
		lookup_expr='icontains'
	)



	class Meta:
		model = PersonRecord
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []