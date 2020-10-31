"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from perfis import views
from usuarios.views import RegistrarUsuarioView
from timelines.views import RealizaPostagemView
from django.contrib.auth import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('perfil/<int:perfil_id>', views.exibir, name = 'exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name = 'convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar', views.recusar, name='recusar'),
    path('perfil/<int:perfil_id>/desfazer', views.desfazer, name = 'desfazer'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),

    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
    path('login/', v.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='login.html'), name='logout'),

    path('perfil/<int:perfil_id>/postar', RealizaPostagemView.as_view(), name='postar'),
]
