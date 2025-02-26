"""
URL configuration for Duo_express_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import home,transport_aerien,transport_bateau,calculatrice,achat_international,achat_billet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aerien',transport_aerien,name='avion'),
    path('bateau',transport_bateau,name='bateau'),
    path('calcul',calculatrice,name='calculatrice'),
    path('achat',achat_international,name='achat'),
    path('billet',achat_billet,name='billet'),
   # path('whatsapp/<int:service_id>/', whatsapp_redirect, name='whatsapp_redirect'),
]
