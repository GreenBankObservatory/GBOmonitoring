from django.urls import include
from django.urls import path
from website.views.data import *


urlpatterns = [
    path("plotly-test/", view_plotly),
]