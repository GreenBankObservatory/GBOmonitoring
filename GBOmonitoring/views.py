from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from prometheus.forms import QueryForm

#from django.views import generic

from django.shortcuts import render


# Create your views here.

from django.views.generic import TemplateView

#class landing_page(TemplateView):
#    template_name = 'landing.html'

def landing_page(request):
    # only call the query if the user submitted something.
    form = QueryForm()
    if request.method == "GET":
        if request.GET.get("submit") == "Submit":
            return query(request)

    return render(request, "landing.html", {"form": form})