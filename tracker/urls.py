from django.urls import path

from . import views

urlpatterns = [
    path('', views.sightings),
    path('<str:UniqueID>/', views.update_sighting, name = 'update'),
    path('add/', views.sightings_add, name='add'),
    path('stats/', views.sightings_stats),
    path('<unique_squirrel_id>/', views.sightings_edit, name='edit'),
    path('map/',views.map),
 ]
