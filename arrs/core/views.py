from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

import core.models

def auth(request):
    pass

def index(request):
    template = loader.get_template("login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template("dashboard.html")
    #TODO populate this with relevant information; see dashbooard.html TODOs
    event_top_six={
    "VPO": core.models.getEventTopComps("VPO", 6),
    "NPO": core.models.getEventTopComps("NPO", 6)
    }
    context = {
    "vpo_top":event_top_six["VPO"]
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
