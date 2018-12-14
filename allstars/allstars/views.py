from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import *

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
		return AllStar.objects.all().order_by('person_record')

class AllStarDetailView(generic.DetailView):
	model = PersonRecord
	context_object_name = 'all_star_player'
	template_name = 'allstars/allstardetail.html'