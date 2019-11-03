from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

import models

def index(request):
    #TODO figure out if this is correct way to implement a secure login.
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username, password=password)

    if user is not None:
        login(request, user)
        #redirect
    else:
        #error?
    #template = loader.get_template("login.html")
    #context = {}
    #return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template("dashboard.html")
    #TODO populate this with relevant information; see dashbooard.html TODOs
    event_top_six={
    "VPO": models.getEventTopComps("VPO", 6),
    "NPO": models.getEventTopComps("NPO", 6)
    }
    context = {
    rankings:event_top_six
    }
    return HttpResponse(template.render(context, request))

def viewRounds(request):
    template = loader.get_template("records.html")
    context = {}
    return HttpResponse(template.render(context, request))

def addRound(request):
    template = loader.get_template("addRound.html")
    #TODO populate this with relevant information; see addRound.html TODOs
    context = {}
    return HttpResponse(template.render(context, request))


#STAGE II
def viewReports(request):
    pass

def addReport(request):
    pass
