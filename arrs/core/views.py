import json
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import core.models

def load_component(request, componentName, context=None):
    if context is None:
        context = {} #if no context dict is passed, use empty dict
    comp_template = loader.get_template("components/" + componentName)
    return comp_template.render(context, request)
    
@login_required
def dashboard(request):
    template = loader.get_template("dashboard.j2")
    #vpo_pie_data = core.models.getCompWinDataSets(tevent="VPO")


    #TODO: Restore visualizations
    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
    }

    return HttpResponse(template.render(context, request))

@login_required
def viewCompetitors(request):
    template = loader.get_template("viewCompetitors.j2")
    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
        "comps": core.models.getComps()
    }
    return HttpResponse(template.render(context, request))

@login_required
def viewRounds(request):
    template = loader.get_template("viewRounds.j2")
    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
        "rounds": core.models.getViewRounds("VPO")
    }
    return HttpResponse(template.render(context, request))

@login_required
def viewTournaments(request):
    template = loader.get_template("viewTournaments.j2")
    
    tournament_data = []
    for t in core.models.Tournament.objects.all():
        tournament_data.append({
            "name": t.get_name(),
            "location": t.get_location(),
            "year": t.get_date().year
        })

    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
        "tournaments": tournament_data
    }
    return HttpResponse(template.render(context, request))

@login_required
def addRound(request):
    template = loader.get_template("addRound.j2")
    #TODO populate this with relevant information; see addRound.html TODOs
    context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2")
    }
    return HttpResponse(template.render(context, request))
