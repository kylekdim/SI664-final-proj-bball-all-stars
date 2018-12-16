from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import *
from django.db.models import Count, F
from django.db.models import Aggregate

def index(request):
   return HttpResponse("Hello, world. You're at the Basketball All-Stars index.")

class HomePageView(generic.TemplateView):
	template_name = 'allstars/home.html'

class AboutPageView(generic.TemplateView):
	template_name = 'allstars/about.html'

class AllStarListView(generic.ListView):
	model = AllStar
	context_object_name = 'all_stars_list'
	template_name = 'allstars/allstarslist.html'
	paginate_by = 100

	def get_queryset(self):
		return AllStar.objects.select_related('person_record', 'league').values('person_record__person_record_id', 'person_record__first_name', 'person_record__last_name').order_by().distinct()

class AllStarDetailView(generic.DetailView):
	model = PersonRecord
	context_object_name = 'person_list'
	template_name = 'allstars/allstardetail.html'

	def get_context_data(self, **kwargs):
		context = super(AllStarDetailView, self).get_context_data(**kwargs)
		context['all_star_list'] = AllStar.objects.select_related('league').values().filter(person_record__person_record_id=self.kwargs['pk']).order_by('year')
		print(context)
		# And so on for more models
		return context

class TeamListView(generic.ListView):
	model = Team
	context_object_name = 'team_list'
	template_name = 'allstars/teamlist.html'
	paginate_by = 40

	def get_queryset(self):
		return Team.objects.all().select_related('league').values('team_id', 'league__league_abbrev', 'name').order_by('league__league_abbrev', 'name')


class TeamDetailView(generic.DetailView):
	model = Team
	context_object_name = 'team_list'
	template_name = 'allstars/teamdetail.html'

	def get_queryset(self):
		return Team.objects.select_related('league').values('team_id', 'league__league_abbrev', 'name')

	def get_context_data(self, **kwargs):

		context = super(TeamDetailView, self).get_context_data(**kwargs)
		#print(team_pk)
		context['team_stat_list'] = TeamStat.objects.select_related('team').filter(team__team_id=self.kwargs['pk'])
		print(context)
		# And so on for more models
		return context

class PersonListView(generic.ListView):
	model = PersonRecord
	context_object_name = 'person_list'
	template_name = 'allstars/personlist.html'
	paginate_by = 200

	def get_queryset(self):
		return PersonRecord.objects.all().order_by('last_name')


class PersonDetailView(generic.DetailView):
	model = PersonRecord
	context_object_name = 'person_record_list'
	template_name = 'allstars/persondetail.html'

	def get_queryset(self):
		return PersonRecord.objects.select_related('league').values()

	def get_context_data(self, **kwargs):

		context = super(PersonDetailView, self).get_context_data(**kwargs)
		#print(team_pk)
		context['team_align_list'] = TeamAlign.objects.select_related('person_record', 'league', 'team').values('league__league_abbrev', 'team__name', 'year', 'stint', 'games_played', 'minutes', 'points', 'assists').filter(person_record__person_record_id=self.kwargs['pk']).order_by('year')
		context['coach_list'] = Coach.objects.select_related('person_record', 'league', 'team').values('league__league_abbrev', 'team__name', 'year', 'won', 'lost').filter(person_record__person_record_id=self.kwargs['pk']).order_by('year')
		print(context)
		# And so on for more models
		return context
















