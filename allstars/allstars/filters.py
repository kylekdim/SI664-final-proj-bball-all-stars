import django_filters
from allstars.forms import SearchForm
from allstars.models import *


class PersonRecordFilter(django_filters.FilterSet):
	person_id_long = django_filters.CharFilter(
		field_name='person_id_long',
		label='Person ID (Long)',
		lookup_expr='icontains'
	)

	first_name = django_filters.CharFilter(
		field_name='first_name',
		label='First Name',
		lookup_expr='icontains'
	)

	middle_name = django_filters.CharFilter(
		field_name='middle_name',
		label='Middle Name',
		lookup_expr='icontains'
	)

	last_name = django_filters.CharFilter(
		field_name='last_name',
		label='Last Name',
		lookup_expr='icontains'
	)

	full_given_name = django_filters.CharFilter(
		field_name='full_given_name',
		label='Full Given Name',
		lookup_expr='icontains'
	)

	name_suffix = django_filters.CharFilter(
		field_name='name_suffix',
		label='Name Suffix',
		lookup_expr='icontains'
	)

	nickname = django_filters.CharFilter(
		field_name='nickname',
		label='Nickname',
		lookup_expr='icontains'
	)

	pos = django_filters.CharFilter(
		field_name='pos',
		label='Position',
		lookup_expr='icontains'
	)

	height = django_filters.NumberFilter(
		field_name='height',
		label='Height (Inches)',
		lookup_expr='exact'
	)

	weight = django_filters.NumberFilter(
		field_name='weight',
		label='Weight (lbs)',
		lookup_expr='exact'
	)

	college = django_filters.CharFilter(
		field_name='college',
		label='College',
		lookup_expr='icontains'
	)

	birthdate = django_filters.NumberFilter(
		field_name='birthdate',
		label='Birthdate (YYYY-MM-DD)',
		lookup_expr='icontains'
	)
	birth_city = django_filters.CharFilter(
		field_name='birth_city',
		label='Birth City',
		lookup_expr='icontains'
	)

	birth_state = django_filters.CharFilter(
		field_name='birth_state',
		label='Birth State',
		lookup_expr='icontains'
	)

	birth_country = django_filters.CharFilter(
		field_name='birth_country',
		label='Birth Country',
		lookup_expr='icontains'
	)

	high_school = django_filters.CharFilter(
		field_name='high_school',
		label='High School',
		lookup_expr='icontains'
	)
	
	hs_city = django_filters.CharFilter(
		field_name='hs_city',
		label='High School City',
		lookup_expr='icontains'
	)

	hs_state = django_filters.CharFilter(
		field_name='hs_state',
		label='High School State',
		lookup_expr='icontains'
	)

	hs_country = django_filters.CharFilter(
		field_name='hs_country',
		label='High School Country',
		lookup_expr='icontains'
	)

	death_date = django_filters.NumberFilter(
		field_name='death_date',
		label='Death Date (YYYY-MM-DD)',
		lookup_expr='icontains'
	)

	race = django_filters.CharFilter(
		field_name='race',
		label='Race',
		lookup_expr='icontains'
	)

	teams_as_coach = django_filters.ModelChoiceFilter(
		field_name='teams_as_coach',
		label='Team(s) as Coach',
		queryset=Team.objects.all().order_by('name'),
		lookup_expr='exact'
	)

	teams_as_player = django_filters.ModelChoiceFilter(
		field_name='teams_as_player',
		label='Team(s) as Player',
		queryset=Team.objects.all().order_by('name'),
		lookup_expr='exact'
	)

	class Meta:
		model = PersonRecord
		queryset = PersonRecord.objects.values('person_record_id', 'first_name', 'last_name').order_by('last_name').distinct()
		context_object_name = 'person_record_list'
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []