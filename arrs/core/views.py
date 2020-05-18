import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import core.models
import core.forms

def load_component(request, componentName, context=None):
    if context is None:
        context = {} #if no context dict is passed, use empty dict
    comp_template = loader.get_template("components/" + componentName)
    return comp_template.render(context, request)
    
@login_required
def dashboard(request):
    template = loader.get_template("dashboard.j2")

    #TODO: Restore visualizations
    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
    }

    return HttpResponse(template.render(context, request))

@login_required
def viewCompetitors(request):
    template = loader.get_template("viewCompetitors.j2")

    comp_data = []
    for c in core.models.Comp.objects.all():
        comp_data.append({
            "name": c.get_name(),
            "num_rounds": len(c.round_set.all())
        })

    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
        "comps": comp_data
    }
    return HttpResponse(template.render(context, request))

@login_required
def viewRounds(request):
    template = loader.get_template("viewRounds.j2")

    round_data = []
    for r in core.models.Round.objects.all():
        data = {
            "competitor": r.get_debater_name(), 
            "tournament": r.get_tournament_name(),
            "opponent": r.get_opponent(),
            "event": r.get_event()
        }
        data["result"] = ("Loss", "Win")[r.get_won()]
        round_data.append(data)

    context = {
        "comp_sidebar": load_component(request, "sidebar.j2"),
        "comp_navbar": load_component(request, "navbar.j2"),
        "rounds": round_data
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
def addComp(request):
    if request.method == "POST":
        form = core.forms.CompForm(request.POST)
        if form.is_valid():
            try:
                new_c_model = core.models.Comp(name=form.cleaned_data['name'])
                new_c_model.save()
                message = "Successfully added Competitor: {}".format(form.cleaned_data['name'])
            except Exception as e:
                message = "Error adding Competitor to database"

        return redirect('/core/viewComp')
    else:
        template = loader.get_template("addComp.j2")
        context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2"),
            "form": core.forms.CompForm()
        }
        return HttpResponse(template.render(context, request))

@login_required
def addTournament(request):
    if request.method == "POST":
        form = core.forms.TournamentForm(request.POST)
        if form.is_valid():
            try:
                new_t_model = core.models.Tournament(
                    name=form.cleaned_data['name'],
                    location=form.cleaned_data['location'],
                    date=form.cleaned_data['date']
                )
                new_t_model.save()
            except Exception as e:
                print("Error saving tournament to database", e)
        else:
            print("Invalid form data")
    
        return redirect('/core/viewTournaments')
    else:
        template = loader.get_template("addTournament.j2")
        context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2"),
            "form": core.forms.TournamentForm()
        }
        return HttpResponse(template.render(context, request))

@login_required
def addRound(request):
    if request.method == "POST":
        form = core.forms.RoundForm(request.POST)
        if form.is_valid():
            try:
                new_r_model = core.models.Round(
                    debater=form.cleaned_data["debater"],
                    tournament=form.cleaned_data["tournament"],
                    opponent=form.cleaned_data["opponent"],
                    bracket=form.cleaned_data["bracket"],
                    event=form.cleaned_data["event"],
                    won=form.cleaned_data["won"],
                    position=form.cleaned_data["position"]
                )
                new_r_model.save()
            except Exception as e:
                print("Error saving round to database", e)
        else:
            print("Invalid form data")
        return redirect('/core/viewRounds')
    else:
        template = loader.get_template("addRound.j2")
        context = {
            "comp_sidebar": load_component(request, "sidebar.j2"),
            "comp_navbar": load_component(request, "navbar.j2"),
            "form": core.forms.RoundForm()
        }
        return HttpResponse(template.render(context, request))
