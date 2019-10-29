from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello world. This is the ARRS index view.")

def login(request):
    #TODO figure out if this is correct way to implement a secure login.
    template = loader.get_template("login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template("dashboard.html")
    #TODO populate this with relevant information; see dashbooard.html TODOs
    context = {}
    return HttpResponse(template.render(context, request))

def seeRounds(request):
    pass

def seeReports(request):
    pass

def addRound(request):
    template = loader.get_template("addRound.html")
    #TODO populate this with relevant information; see addRound.html TODOs
    context = {}
    return HttpResponse(template.render(context, request))

def addReport(request):
    pass
