from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detect', views.runDetector, name='runDetector'),
    path('delete', views.deleteFiles, name='deleteUploads'),
    path('upload', views.loadImage, name='loadImage'),

]
