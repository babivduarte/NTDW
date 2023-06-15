from django.forms import ModelForm
from .models import *
from django import forms

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"

class CronogramaForm(ModelForm):
    class Meta:
        model = Cronograma
        fields = "__all__"

class AvaliadorForm(ModelForm):
    class Meta:
        model = Avaliador
        fields = "__all__"

class PremioForm(ModelForm):
    class Meta:
        model = Premio
        fields = "__all__"

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"

class EnviarProjetoForm(ModelForm):
    class Meta:
        model = EnviarProjeto
        fields = "__all__"

class AvaliarProjetoForm(ModelForm):
    projeto = forms.ModelChoiceField(
        queryset=Projeto.objects.all(),
        label='Projeto',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=None,
    )
    class Meta:
        model = AvaliarProjeto
        fields = ['parecer', 'nota', 'avaliador','projeto']