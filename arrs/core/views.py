import json
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import core.models

def get_component(filename):
    result = ""
    print(os.getcwd())
    with open(filename, "r") as component:
        for l in component.readlines():
            result = result + l
    return result.replace("\n", "")

def load_component(request, componentName, context=None):
    if context is None:
        context = {} #if no context dict is passed, use empty dict
    comp_template = loader.get_template("components/" + componentName)
    return comp_template.render(context, request)
    
@login_required
def dashboard(request):
    template = loader.get_template("dashboard.j2")
    vpo_pie_data = core.models.getCompWinDataSets(tevent="VPO")

    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
        "vpo_top": core.models.getEventTopComps("VPO", 6),
        "npo_top": core.models.getEventTopComps("NPO", 6),
        "vpo_pie_names": vpo_pie_data["names"],
        "vpo_pie_wins": vpo_pie_data["wins"],
    }

    return HttpResponse(template.render(context, request))

@login_required
def viewCompetitors(request):
    template = loader.get_template("viewCompetitors.j2")
    context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2"),
            "comps":[]
    }
    return HttpResponse(template.render(context, request))

@login_required
def viewRounds(request):
    template = loader.get_template("viewRounds.j2")
    context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2"),
            "comps":[]
    }
    return HttpResponse(template.render(context, request))

@login_required
def addRound(request):
    template = loader.get_template("addRound.html")
    #TODO populate this with relevant information; see addRound.html TODOs
    context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2")
    }
    return HttpResponse(template.render(context, request))

#STAGE II
@login_required
def viewReports(request):
    pass

@login_required
def addReport(request):
    pass
