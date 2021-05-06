from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import User

def index(request):
    return render(request, 'weather/index.html')

def login(request): #if user exists, goto user page, else create user then goto user page
    username = request.POST['username']
    try:
        user = User.objects.get(username=username)
    except:
        user = User.objects.create(username=username)
    return HttpResponseRedirect(reverse('weather:userpage', args=[user.id]))

def userpage(request, user_id):
    context = {
        'user': get_object_or_404(User, pk=user_id)
    }
    return render(request, 'weather/userpage.html/', context)