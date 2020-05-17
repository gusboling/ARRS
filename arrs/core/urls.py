from django.urls import path

from . import views

#TODO eliminate index page/url routing?
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('addRound', views.addRound, name="addRound"),
    path('addComp', views.addComp, name="addComp"),
    path('addTournament', views.addTournament, name="addTournament"),
    path('viewRounds', views.viewRounds, name="viewRound"),
    path('viewComp', views.viewCompetitors, name="viewComp"),
    path('viewTournaments', views.viewTournaments, name="viewTournaments")
]
