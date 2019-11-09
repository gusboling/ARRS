from django.urls import path

from . import views

#TODO eliminate index page/url routing?
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('addRound', views.addRound, name="addRound"),
    path('viewRounds', views.viewRounds, name="viewRound"),
]
