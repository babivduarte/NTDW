from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.

def index(request):
    return HttpResponse("Hello Word")

def novoAutor(request):
    data = {}
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listAutores')

    data['form'] = form
    return render(request, 'Autor/novo_autor.html', data)

def listAutores(request):
    data = {}
    data['autores'] = Autor.objects.all()
    return render(request, 'Autor/list_autores.html', data)

def listCronogramas(request):
    data = {}
    data['cronogramas'] = Cronograma.objects.all()
    return render(request, 'Cronograma/list_cronogramas.html', data)

def novoCronograma(request):
    data = {}
    form = CronogramaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listCronogramas')

    data['form'] = form
    return render(request, 'Cronograma/novo_cronograma.html', data)

def listAvaliadores(request):
    data = {}
    data['avaliadores'] = Avaliador.objects.all()
    return render(request, 'Avaliador/list_avaliadores.html', data)

def novoAvaliador(request):
    data = {}
    form = AvaliadorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listAvaliadores')

    data['form'] = form
    return render(request, 'Avaliador/novo_avaliador.html', data)

def listPremios(request):
    data = {}
    data['premios'] = Premio.objects.all()
    return render(request, 'Premio/list_premios.html', data)

def novoPremio(request):
    data = {}
    form = PremioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listPremios')

    data['form'] = form
    return render(request, 'Premio/novo_premio.html', data)

def listProjetos(request):
    data = {}
    data['projetos'] = Projeto.objects.all()
    return render(request, 'Projeto/list_projetos.html', data)

def novoProjeto(request):
    data = {}
    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listProjetos')

    data['form'] = form
    return render(request, 'Projeto/novo_projeto.html', data)

def projetosEnviados(request):
    data = {}
    data['projetosEnviados'] = EnviarProjeto.objects.all()
    return render(request, 'Projeto/projetos_enviados.html', data)

def enviarProjeto(request):
    data = {}
    form = EnviarProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('projetosEnviados')

    data['form'] = form
    return render(request, 'Projeto/enviar_projeto.html', data)

def projetosAvaliados(request):
    data = {}
    data['projetosAvaliados'] = AvaliarProjeto.objects.all()
    return render(request, 'Projeto/projetos_avaliados.html', data)

def avaliarProjeto(request):
    data = {}
    form = AvaliarProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('projetosAvaliados')

    data['form'] = form
    return render(request, 'Projeto/avaliar_projeto.html', data)

