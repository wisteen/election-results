from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load-lgas/', views.load_lgas, name='ajax_load_lgas'),
    path('store-results/', views.store_results, name='store_results'),
]
