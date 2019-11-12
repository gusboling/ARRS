from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import core.models

@login_required
def dashboard(request):
    template = loader.get_template("dashboard.html")
    #TODO populate this with relevant information; see dashbooard.html TODOs
    event_top_six={
        "VPO": core.models.getEventTopComps("VPO", 6),
        "NPO": core.models.getEventTopComps("NPO", 6)
    }


    context = {
        "vpo_top":event_top_six["VPO"],
        "npo_top":event_top_six["NPO"],
        "testArray": [25, 12, 15, 11, 8],
    }
    return HttpResponse(template.render(context, request))

@login_required
def viewRounds(request):
    template = loader.get_template("records.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def addRound(request):
    template = loader.get_template("addRound.html")
    #TODO populate this with relevant information; see addRound.html TODOs
    context = {}
    return HttpResponse(template.render(context, request))

#STAGE II
@login_required
def viewReports(request):
    pass

@login_required
def addReport(request):
    pass
