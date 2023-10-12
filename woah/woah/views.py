from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from prometheus.forms import QueryForm

from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, "index.html")

def landing_page(request):
    form = QueryForm()
    if request.method == "GET":
        if request.GET.get("submit") == "Submit":
            return query(request)

    return render(request, "prometheus/landing.html", {"form": form})