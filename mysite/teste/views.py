from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .serializer import *
from rest_framework import viewsets
import coreapi

# Create your views here.
#------- APIs
class AutorViewApi(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CronogramaViewApi(viewsets.ModelViewSet):
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer

class AvaliadorViewApi(viewsets.ModelViewSet):
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializer

class PremioViewApi(viewsets.ModelViewSet):
    queryset = Premio.objects.all()
    serializer_class = PremioSerializer

class ProjetoViewApi(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class ProjetoEnviadoViewApi(viewsets.ModelViewSet):
    queryset = EnviarProjeto.objects.all()
    serializer_class = EnviarProjetoSerializer

class ProjetoAvaliadoViewApi(viewsets.ModelViewSet):
    queryset = AvaliarProjeto.objects.all()
    serializer_class = AvaliarProjetoSerializer


#-----------------------------CRUDS-------------------------------------
def index(request):
    return HttpResponse("Hello Word")

def novoAutor(request):
    form = AutorForm()
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            client = coreapi.Client()
            schema = client.get("http://127.0.0.1:8000/teste/docs")

            action = ["autores", "create"]
            params = {
                "nome": form.cleaned_data['nome'],
                "idade": form.cleaned_data['idade'],
                "cpf": form.cleaned_data['cpf'],
                "telefone": form.cleaned_data['telefone'],
                "email": form.cleaned_data['email'],
            }
            client.action(schema, action, params=params)
        return redirect('listAutores')
    elif request.method == 'GET':
        return render(request, 'Autor/novo_autor.html', {'form': form})

def listAutores(request):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs")

    action = ["autores", "list"]
    result = client.action(schema, action)
    return render(request, 'Autor/list_autores.html', {'autores': result})

def listCronogramas(request):
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs")

    # Interact with the API endpoint
    action = ["cronogramas", "list"]
    result = client.action(schema, action)
    return render(request, 'Cronograma/list_cronogramas.html', {'cronogramas': result})

def novoCronograma(request):
    form = CronogramaForm()
    if request.method == 'POST':
        form = CronogramaForm(request.POST)
        if form.is_valid():
            client = coreapi.Client()
            schema = client.get("http://127.0.0.1:8000/teste/docs")

            action = ["cronogramas", "create"]
            params = {
                "dataInicio": form.cleaned_data['dataInicio'].isoformat(),
                "dataFim": form.cleaned_data['dataFim'].isoformat(),
                "descricao": form.cleaned_data['descricao'],
            }
            client.action(schema, action, params=params)
        return redirect('listCronogramas')
    elif request.method == 'GET':
        return render(request, 'Cronograma/novo_cronograma.html', {'form': form})

def listAvaliadores(request):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs")

    action = ["avaliadores", "list"]
    result = client.action(schema, action)
    return render(request, 'Avaliador/list_avaliadores.html', {'avaliadores': result})

def novoAvaliador(request):
    form = AvaliadorForm()
    if request.method == 'POST':
        form = AvaliadorForm(request.POST)
        if form.is_valid():
            client = coreapi.Client()
            schema = client.get("http://127.0.0.1:8000/teste/docs")

            action = ["avaliadores", "create"]
            params = {
                "nome": form.cleaned_data['nome'],
                "idade": form.cleaned_data['idade'],
                "cpf": form.cleaned_data['cpf'],
                "areaFormacao": form.cleaned_data['areaFormacao'],
            }
            client.action(schema, action, params=params)
        return redirect('listAvaliadores')
    elif request.method == 'GET':
        return render(request, 'Avaliador/novo_avaliador.html', {'form': form})

def listPremios(request):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs")

    action = ["premios", "list"]
    result = client.action(schema, action)
    return render(request, 'Premio/list_premios.html', {'premios': result})

def novoPremio(request):
    form = PremioForm()
    if request.method == 'POST':
        form = PremioForm(request.POST)
        if form.is_valid():
            client = coreapi.Client()
            schema = client.get("http://127.0.0.1:8000/teste/docs")

            action = ["premios", "create"]
            params = {
                "nome": form.cleaned_data['nome'],
                "descricao": form.cleaned_data['descricao'],
                "ano": form.cleaned_data['ano'],
                "cronograma_fk": form.cleaned_data['cronograma_fk'].id,
            }
            client.action(schema, action, params=params)
        return redirect('listPremios')
    elif request.method == 'GET':
        return render(request, 'Premio/novo_premio.html', {'form': form})

def listProjetos(request):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs")

    action_autores = ["autores", "list"]
    result_autores = client.action(schema, action_autores)
    action = ["projetos", "list"]
    result = client.action(schema, action)
    return render(request, 'Projeto/list_projetos.html', {'projetos': result, 'autores': result_autores})


def novoProjeto(request):
    form = ProjetoForm()
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            client = coreapi.Client()
            schema = client.get("http://127.0.0.1:8000/teste/docs")

            action = ["projetos", "create"]
            params = {
                "nome": form.cleaned_data['nome'],
                "descricao": form.cleaned_data['descricao'],
                "ano": form.cleaned_data['ano'],
                "cronograma_fk": form.cleaned_data['cronograma_fk'].id,
            }
            client.action(schema, action, params=params)
        return redirect('listPremios')
    elif request.method == 'GET':
        return render(request, 'Premio/novo_premio.html', {'form': form})

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

