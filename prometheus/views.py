from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("Hello, Clarice. I will put the prometheus connection here.")


class query_page(TemplateView):
    template_name = 'prom_query.html'