from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name='home'),
	path('movie_list/',views.movie_list,name='movie_list'),
	path('movie_detail/',views.movie_detail,name='movie_detail'),
	]