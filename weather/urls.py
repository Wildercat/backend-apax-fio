from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.userpage, name='userpage'),
    path('login/', views.login, name='login'),
    path('<int:user_id>/add_location', views.add_location, name='add_location'),
    path('<int:user_id>/location/<int:location_id>/delete', views.delete_location, name='delete_location'),
    path('<int:user_id>/location/<int:location_id>/update', views.update_location, name='update_location'),
    path('<int:user_id>/location/update_all', views.update_all_location, name='update_all_location')
]