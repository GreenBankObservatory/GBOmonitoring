from django.http import Http404
from django.shortcuts import render

def view_plotly(request):
    context = {}
    return render(request, "data/plotly.html", context)