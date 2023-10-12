# Django imports
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
import django_cas_ng.views

# Local imports
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('old_landing/', views.landing_page, name='landing'),
    path("alert/", include("alert.urls")),
    path('prometheus/', include('prometheus.urls')),
    path('util/', include('util.urls')),
    path("visualization/", include("visualization.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('debug/', include(debug_toolbar.urls)),
    ]