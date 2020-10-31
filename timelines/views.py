from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from perfis.models import Perfil
from timelines.forms import RealizaPostagemForm

class RealizaPostagemView(View):
    def get(self, request):
        return render(request, 'postagem.html')

    def post(self, request):
        form = RealizaPostagemForm(request.POST)
        dados = form.cleaned_data

		form.save()

        return redirect('timeline')