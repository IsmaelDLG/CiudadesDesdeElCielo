from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crawl', views.runSpiders, name='runSpiders'),
]