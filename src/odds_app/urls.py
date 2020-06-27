"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views


# api_urlpatterns = [
#     path('accounts/', include('rest_registration.api.urls')),
#     url(r'^api-auth/', include('rest_framework.urls'))
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("odds.urls")),  # add this # add this

    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),
    path('index', views.old_index, name='index_old'),
    #path('api/v1/', include(api_urlpatterns)),
]

