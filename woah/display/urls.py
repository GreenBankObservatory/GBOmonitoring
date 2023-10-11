from django.urls import path, re_path
from ...woah-temp.dashboards import views
 
urlpatterns = [
    path("", views.home, name="home"),
    path("ZtiltPos", views.ZtiltPos, name="ZtiltPos"),
    path("OSS", views.OSS, name="OSS"),
    ]