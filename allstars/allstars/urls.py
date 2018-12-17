from django.urls import path, re_path
from . import views

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('aslist/', views.AllStarListView.as_view(), name='all_stars'),
   path('aslist/<int:pk>/', views.AllStarDetailView.as_view(), name='all_star_detail'),
   path('teamlist/', views.TeamListView.as_view(), name='teams'),
   path('teamlist/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
   path('personlist/', views.PersonListView.as_view(), name='people'),
   path('personlist/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
   path('personlist/new/', views.PersonCreateView.as_view(), name='person_new'),
   path('personlist/<int:pk>/delete/', views.PersonDeleteView.as_view(), name='person_delete'),
   path('personlist/<int:pk>/update/', views.PersonUpdateView.as_view(), name='person_update')

   #The two URLs below were added during the midterm:
   #path('countries/', views.CountryAreaListView.as_view(), name='countries'),
   #path('countries/<int:pk>/', views.CountryAreaDetailView.as_view(), name='country_detail'),
]