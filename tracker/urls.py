from django.urls import path

from . import views

urlpatterns = [
    path('', views.tracker),
    path('<str:UniqueID>/', views.update_tracker, name = 'update'),
    path('add/', views.add, name='add'),
    path('stats/', views.stats),
    path('<unique_squirrel_id>/', views.sightings_edit, name='edit'),
    path('map/',views.map),
 ]
