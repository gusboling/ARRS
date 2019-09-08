from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. This is the ARRS index view.")

def dashboard(request):
    pass

def seeRounds(request):
    pass

def seeReports(request):
    pass

def addRound(request):
    pass

def addReport(request):
    pass
