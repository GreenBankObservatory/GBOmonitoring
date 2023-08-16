from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("template/", views.template_page.as_view(), name='prom_template')
]