from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronograma
        fields = "__all__"

class AvaliadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliador
        fields = "__all__"

class PremioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premio
        fields = "__all__"

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = "__all__"

class EnviarProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnviarProjeto
        fields = "__all__"

class AvaliarProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliarProjeto
        fields = "__all__"