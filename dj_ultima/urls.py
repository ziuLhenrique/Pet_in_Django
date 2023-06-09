"""
URL configuration for FormularioDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

#PARA INCLUIR RESERVA URL
from django.urls import include

#PRECISA ADICIONAR INICIO
from base.views import inicio
from base.views import contato

urlpatterns = [
	#PRECISA POR A PATH
    path("", inicio),
    path("contato/", contato),
    path("admin/", admin.site.urls),
	#ADICIONAR RESERVA
	path("reserva/", include('reserva.urls', namespace='reserva')),
    #ADICIONAR REST
    path("api-auth/", include('rest_framework.urls')),
    path("api/", include('rest_api.urls', namespace = 'api')),
]
