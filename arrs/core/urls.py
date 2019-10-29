from django.urls import path

from . import views

#TODO eliminate index page/url routing?
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('addRound', views.addRound, name="addRound")
]
