from django.urls import path, re_path
from . import views

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('aslist/', views.AllStarListView.as_view(), name='all_stars'),
   path('aslist/<int:pk>/', views.AllStarDetailView.as_view(), name='all_star_detail'),
]