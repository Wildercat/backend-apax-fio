from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import User,Location

import requests

def index(request):
    return render(request, 'weather/index.html')

def login(request): #if user exists, goto user page, else create user then goto user page
    username = request.POST['username']
    try:
        user = User.objects.get(username=username)
    except:
        user = User.objects.create(username=username)
    return HttpResponseRedirect(reverse('weather:userpage', args=[user.id]))


def update(location_id):
    def lookup(zip_code): #api call
        url = 'http://api.openweathermap.org/data/2.5/weather?zip='+ zip_code +',us&units=imperial&appid=9d9e3d0b51cb088b9905bacc4328c9c2'
        result = requests.get(url)
        # print(result.json())
        return result.json()
    location = get_object_or_404(Location, pk=location_id)
    data = lookup(location.zip_code)
    print(data)

    location.location_name = data['name']
    location.weather_main = data['weather'][0]['main']
    location.weather_desc = data['weather'][0]['description']
    location.weather_icon = data['weather'][0]['icon']
    location.main_temp = data['main']['temp']
    location.main_temp_min = data['main']['temp_min']
    location.main_temp_max = data['main']['temp_max']
    
    location.save()

def add_location(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    location = user.location_set.create(zip_code=request.POST['zip_code'])
    update(location.id)
    return HttpResponseRedirect(reverse('weather:userpage', args=[user.id]))

def delete_location(request, user_id, location_id):
    # user = get_object_or_404(User, pk=user_id)
    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    return HttpResponseRedirect(reverse('weather:userpage', args=[user_id]))

def userpage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user,
        'location_list': user.location_set.all()
    }
    return render(request, 'weather/userpage.html/', context)