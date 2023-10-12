# Classic imports
import pandas as pd

# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# Local imports
from visualization.plot.dash import *
from visualization.ODS.core import *

def home(request):
    return HttpResponse("Welcome to the alerts home page")

def BugReport(request):
    return HttpResponse("Welcome to the bug reports page")