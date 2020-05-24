from django.shortcuts import render
from django.http import HttpResponse
from . import models as model
def home(request):
	context = {}
	return render(request,'home/home.html',{"data" : context})
def movie_list(request):
	context = model.movie.objects.all()
	return render(request,'home/movie_list.html',{"data" : context})
def movie_detail(request):
	context = model.movie.objects.all()
	return render(request,'home/movie_detail.html',{"data" : context})

# Create your views here.
