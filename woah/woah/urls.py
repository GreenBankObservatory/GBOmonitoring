from django.contrib import admin
from django.urls import include, path
from . import views
#import home_page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('old_landing/', views.landing_page, name='landing'),
    path('prometheus/', include('prometheus.urls')),
    path("dashboards/", include("dashboards.urls")),
    path("alerts/", include("alerts.urls")),
]