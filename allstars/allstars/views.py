from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import *
from django.db.models import Count, F
from django.db.models import Aggregate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from allstars.forms import PersonForm, SearchForm

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


@method_decorator(login_required, name='dispatch')
class TeamListView(generic.ListView):
	model = Team
	context_object_name = 'team_list'
	template_name = 'allstars/teamlist.html'
	paginate_by = 40

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Team.objects.all().select_related('league').values('team_id', 'league__league_abbrev', 'name').order_by('league__league_abbrev', 'name')

@method_decorator(login_required, name='dispatch')
class TeamDetailView(generic.DetailView):
	model = Team
	context_object_name = 'team_list'
	template_name = 'allstars/teamdetail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

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

@method_decorator(login_required, name='dispatch')
class PersonCreateView(generic.View):
	model = PersonRecord
	form_class = PersonForm
	success_message = "Person Record created successfully"
	template_name = 'allstars/person_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = PersonForm(request.POST)
		if form.is_valid():
			person = form.save(commit=False)
			person.save()
			#for country in form.cleaned_data['country_area']:
				#HeritageSiteJurisdiction.objects.create(heritage_site=site, country_area=country)
			return redirect(person) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'allstars/person_new.html', {'form': form})

	def get(self, request):
		form = PersonForm()
		return render(request, 'allstars/person_new.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class PersonUpdateView(generic.UpdateView):
	model = PersonRecord
	form_class = PersonForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'person'
	# pk_url_kwarg = 'site_pk'
	success_message = "Person Record updated successfully"
	template_name = 'allstars/person_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		person = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		person.save()

		# Current country_area_id values linked to site
		#old_ids = HeritageSiteJurisdiction.objects\
			#.values_list('country_area_id', flat=True)\
			#.filter(heritage_site_id=site.heritage_site_id)

		# New countries list
		#new_countries = form.cleaned_data['country_area']

		# TODO can these loops be refactored?

		# New ids
		#new_ids = []

		# Insert new unmatched country entries
		#for country in new_countries:
			#new_id = country.country_area_id
			#new_ids.append(new_id)
			#if new_id in old_ids:
				#continue
			#else:
				#HeritageSiteJurisdiction.objects \
					#.create(heritage_site=site, country_area=country)

		# Delete old unmatched country entries
		#for old_id in old_ids:
			#if old_id in new_ids:
				#continue
			#else:
				#HeritageSiteJurisdiction.objects \
					#.filter(heritage_site_id=site.heritage_site_id, country_area_id=old_id) \
					#.delete()

		return HttpResponseRedirect(person.get_absolute_url())
		# return redirect('heritagesites/site_detail', pk=site.pk)

@method_decorator(login_required, name='dispatch')
class PersonDeleteView(generic.DeleteView):
	model = PersonRecord
	success_message = "Person Record deleted successfully"
	success_url = reverse_lazy('person')
	context_object_name = 'person'
	template_name = 'allstars/site_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		#HeritageSiteJurisdiction.objects \
			#.filter(heritage_site_id=self.object.heritage_site_id) \
			#.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())
















