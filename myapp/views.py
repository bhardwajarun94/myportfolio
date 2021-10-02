from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import requests
# Create your views here.

url = "http://api.openweathermap.org/data/2.5/weather?q=Delhi&units=metric&appid=066a97ba6fafcdfa7b0942467078fac9"

def home(request):
	r = requests.get(url).json()
	data = {
		'city':'Delhi',
		'temperature':r['main']['temp'],
		'feels_like': r['main']['feels_like'],
		'humidity': r['main']['humidity'],
		'visibility': r['visibility'],
		'description':r['weather'][0]['main'],
		'icon':r['weather'][0]['icon'],
		'wind_speed':r['wind']['speed'],
	}
	context = {'city_weather':data}
	return render(request,'myapp/index.html',context)


def projects(request):
	context = {}
	projects = Project.objects.all()
	context['projects'] = projects
	return render(request,'myapp/blog-single.html', context)