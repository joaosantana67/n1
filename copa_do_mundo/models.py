from django.db import models


class Selecao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"


class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    selecao = models.ForeignKey(Selecao, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.nome}"


class Juiz(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"


class Partida(models.Model):
    estadio = models.CharField(max_length=100, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    local_de_streaming = models.CharField(max_length=100, blank=True, null=True)

    selecao_casa = models.ForeignKey(Selecao,on_delete=models.SET_NULL,blank=True, null=True, related_name= 'selecao_casa')

    selecao_visitante = models.ForeignKey(Selecao,on_delete=models.SET_NULL,blank=True, null=True,related_name= 'selecao_visitante')

    jogadores_casa = models.ManyToManyField(Jogador, blank=True, related_name='jogadores_time_da_casa')

    jogadores_fora = models.ManyToManyField(Jogador, blank=True, related_name='jogadores_time_de_fora')

    juizes = models.ManyToManyField(Juiz, blank=True)

    def __str__(self):
        return f"{self.selecao_casa} x {self.selecao_visitante}"