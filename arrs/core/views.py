from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello world. This is the ARRS index view.")

def dashboard(request):
    template = loader.get_template(templates/dashboard.html)
    context = {}
    return HttpResponse(template.render(context, request))

def seeRounds(request):
    pass

def seeReports(request):
    pass

def addRound(request):
    pass

def addReport(request):
    pass
