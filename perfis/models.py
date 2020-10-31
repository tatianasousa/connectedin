from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self, convidado=perfil_convidado)
            convite.save()

    def desfazer(self, perfil):
        self.contatos.remove(perfil)
        perfil.contatos.remove(self)

    def pode_convidar(self, perfil):
        nao_pode = self.convite_a_si_mesmo(perfil) or self.ja_eh_contato(perfil) or self.ja_possui_convite(perfil)
        return not nao_pode

    def convite_a_si_mesmo(self, perfil):
        return self == perfil

    def ja_eh_contato(self, perfil):
        return self.contatos.filter(id=perfil.id).exists()

    def ja_possui_convite(self, perfil):
        return (Convite.objects.filter(solicitante=self, convidado=perfil).exists() or Convite.objects.filter(solicitante=perfil, convidado=self).exists())

    def __str__(self):
        return self.nome

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos', on_delete = models.CASCADE)
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos', on_delete = models.CASCADE)

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()

    def recusar(self):
        self.delete()
