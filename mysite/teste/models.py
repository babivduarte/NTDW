from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cronograma(models.Model):
    dataInicio = models.DateField()
    dataFim = models.DateField()
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao

class Avaliador(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=20)
    areaFormacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Premio(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)
    ano = models.IntegerField()
    cronograma = models.ForeignKey(Cronograma, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)
    areaProjeto = models.CharField(max_length=100)
    premio = models.ForeignKey(Premio, on_delete=models.SET_NULL,null=True)
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.nome

class EnviarProjeto(models.Model):
    dataEnvio = models.DateField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)


class AvaliarProjeto(models.Model):
    parecer = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=4,decimal_places=2)
    dataAvaliacao = models.DateField()
    avaliador = models.ManyToManyField(Avaliador)
    projetoEnviado = models.ForeignKey(EnviarProjeto, on_delete=models.CASCADE)
