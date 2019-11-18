import json

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import core.models

@login_required
def dashboard(request):
    template = loader.get_template("dashboard.html")

    vpo_pie_data = core.models.getCompWinDataSets(tevent="VPO")

    context = {
        "vpo_top": core.models.getEventTopComps("VPO", 6),
        "npo_top": core.models.getEventTopComps("NPO", 6),
        "vpo_pie_names": vpo_pie_data["names"],
        "vpo_pie_wins": vpo_pie_data["wins"]
    }

    print(vpo_pie_data["names"])

    return HttpResponse(template.render(context, request))

@login_required
def viewRounds(request):
    template = loader.get_template("viewCompetitors.html")
    context = {"comps":[]}
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
