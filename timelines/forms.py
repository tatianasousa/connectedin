from django import forms
from django.contrib.auth.models import User

class RealizaPostagemForm(forms.Form):
    usuario = forms.CharField(required=True)
    texto = forms.Textarea(required=True)
    criado_em = models.DateTimeField(auto_now_add=True, required=True)