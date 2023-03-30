from django.urls import path        #importando o módulo

from . import views                 #importa tudo o que tá dentro do arquivo views

urlpatterns = [
    path('',views.index, name='index'),       #criando padrões de url
    path('novoAutor/',views.novoAutor, name='novoAutor'),
    path('autores/',views.listAutores, name='listAutores'),
    path('novoCronograma/',views.novoCronograma, name='novoCronograma'),
    path('cronogramas/',views.listCronogramas, name='listCronogramas'),
    path('novoAvaliador/',views.novoAvaliador, name='novoAvaliador'),
    path('avaliadores/',views.listAvaliadores, name='listAvaliadores'),
    path('novoPremio/',views.novoPremio, name='novoPremio'),
    path('premios/',views.listPremios, name='listPremios'),
    path('novoProjeto/',views.novoProjeto, name='novoProjeto'),
    path('projetos/',views.listProjetos, name='listProjetos'),
    path('enviarProjeto/',views.enviarProjeto, name='enviarProjeto'),
    path('projetosEnviados/',views.projetosEnviados, name='projetosEnviados'),
    path('avaliarProjeto/',views.avaliarProjeto, name='avaliarProjeto'),
    path('projetosAvaliados/',views.projetosAvaliados, name='projetosAvaliados')
]

