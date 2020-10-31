from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm

class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if (form.is_valid()):
            dados_form  = form.cleaned_data
            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
            
            perfil = Perfil(nome=usuario.username, telefone=dados_form['telefone'], nome_empresa=dados_form['nome_empresa'], usuario = usuario)
            perfil.save()
            return redirect('index')
        return render(request, self.template_name, {'form' : form})
