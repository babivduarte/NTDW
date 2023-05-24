from django.urls import path, include        #importando o módulo
from . import views                 #importa tudo o que tá dentro do arquivo views
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.documentation import include_docs_urls

router = DefaultRouter(trailing_slash=False)
router.register(r'cronogramas', CronogramaViewApi)
router.register(r'autores', AutorViewApi)
router.register(r'avaliadores', AvaliadorViewApi)
router.register(r'premios', PremioViewApi)
router.register(r'projetos', ProjetoViewApi)
router.register(r'projetos_enviados', ProjetoEnviadoViewApi)
router.register(r'projetos_avaliados', ProjetoAvaliadoViewApi)

urlpatterns = [
    path('',views.index, name='index'),
    path('apis/', include(router.urls)),
    path('docs/', include_docs_urls(title='APIs')),

    path('novoAutor/',views.novoAutor, name='novoAutor'),
    path('autores/',views.listAutores, name='listAutores'),
    path('deletarAutor/<int:id>', views.deleteAutor, name='deletarAutor'),

    path('novoCronograma/',views.novoCronograma, name='novoCronograma'),
    path('cronogramas/',views.listCronogramas, name='listCronogramas'),
    path('deletarCronograma/<int:id>', views.deleteCronograma, name='deletarCronograma'),

    path('novoAvaliador/',views.novoAvaliador, name='novoAvaliador'),
    path('avaliadores/',views.listAvaliadores, name='listAvaliadores'),
    path('deletarAvaliador/<int:id>', views.deleteAvaliador, name='deletarAvaliador'),

    path('novoPremio/',views.novoPremio, name='novoPremio'),
    path('premios/',views.listPremios, name='listPremios'),
    path('deletarPremio/<int:id>', views.deletePremio, name='deletarPremio'),

    path('novoProjeto/',views.novoProjeto, name='novoProjeto'),
    path('projetos/',views.listProjetos, name='listProjetos'),

    path('enviarProjeto/',views.enviarProjeto, name='enviarProjeto'),
    path('projetosEnviados/',views.projetosEnviados, name='projetosEnviados'),

    path('avaliarProjeto/',views.avaliarProjeto, name='avaliarProjeto'),
    path('projetosAvaliados/',views.projetosAvaliados, name='projetosAvaliados')
]

