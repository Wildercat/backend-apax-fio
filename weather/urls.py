from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.userpage, name='userpage'),
    path('login/', views.login, name='login'),
]