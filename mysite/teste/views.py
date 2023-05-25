from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .serializer import *
from rest_framework import viewsets
import coreapi


# Create your views here.
# ------- APIs
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


# -----------------------------CRUDS-------------------------------------
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


def alterarAutor(request, id):
    autor = Autor.objects.get(id=id)
    form = AutorForm(instance=autor)

    if request.method == 'GET':
        return render(request, 'Autor/alterar_autor.html',
                      {'form': form, 'autor': autor})
    elif request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        autor = form.save(commit=False)
        autor.nome = form.cleaned_data['nome']
        autor.idade = form.cleaned_data['idade']
        autor.cpf = form.cleaned_data['cpf']
        autor.telefone = form.cleaned_data['telefone']
        autor.email = form.cleaned_data['email']
        autor.save()

        # Initialize a client & load the schema document
        client = coreapi.Client()
        schema = client.get("http://127.0.0.1:8000/teste/docs")

        # Interact with the API endpoint
        action = ["autores", "update"]
        params = {
            "id": id,
            "nome": form.cleaned_data['nome'],
            "idade": form.cleaned_data['idade'],
            "cpf": form.cleaned_data['cpf'],
            "telefone": form.cleaned_data['telefone'],
            "email": form.cleaned_data['email'],
        }
        client.action(schema, action, params=params)
        return redirect('listAutores')


def listAutores(request):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs")

    action = ["autores", "list"]
    result = client.action(schema, action)
    return render(request, 'Autor/list_autores.html', {'autores': result})


def deleteAutor(request, id):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs/")

    action = ["autores", "delete"]
    params = {
        "id": id,
    }
    result = client.action(schema, action, params=params)
    return redirect('listAutores')


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


def alterarCronograma(request, id):
    cronograma = Cronograma.objects.get(id=id)
    form = CronogramaForm(instance=cronograma)

    if request.method == 'GET':
        return render(request, 'Cronograma/alterar_cronograma.html',
                      {'form': form, 'cronograma': cronograma})
    elif request.method == 'POST':
        form = CronogramaForm(request.POST, instance=cronograma)
        cronograma = form.save(commit=False)
        cronograma.descricao = form.cleaned_data['descricao']
        cronograma.dataInicio = form.cleaned_data['dataInicio']
        cronograma.dataFim = form.cleaned_data['dataFim']
        cronograma.save()

        # Initialize a client & load the schema document
        client = coreapi.Client()
        schema = client.get("http://127.0.0.1:8000/teste/docs")

        # Interact with the API endpoint
        action = ["cronogramas", "update"]
        params = {
            "id": id,
            "dataInicio": form.cleaned_data['dataInicio'].isoformat(),
            "dataFim": form.cleaned_data['dataFim'].isoformat(),
            "descricao": form.cleaned_data['descricao'],
        }
        client.action(schema, action, params=params)
        return redirect('listCronogramas')


def deleteCronograma(request, id):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs/")

    # Interact with the API endpoint
    action = ["cronogramas", "delete"]
    params = {
        "id": id,
    }
    client.action(schema, action, params=params)
    return redirect('listCronogramas')


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


def alterarAvaliador(request, id):
    avaliador = Avaliador.objects.get(id=id)
    form = AvaliadorForm(instance=avaliador)

    if request.method == 'GET':
        return render(request, 'Avaliador/alterar_avaliador.html',
                      {'form': form, 'avaliador': avaliador})
    elif request.method == 'POST':
        form = AvaliadorForm(request.POST, instance=avaliador)
        avaliador = form.save(commit=False)
        avaliador.nome = form.cleaned_data['nome']
        avaliador.idade = form.cleaned_data['idade']
        avaliador.cpf = form.cleaned_data['cpf']
        avaliador.areaFormacao = form.cleaned_data['areaFormacao']
        avaliador.save()

        # Initialize a client & load the schema document
        client = coreapi.Client()
        schema = client.get("http://127.0.0.1:8000/teste/docs")

        # Interact with the API endpoint
        action = ["avaliadores", "update"]
        params = {
            "id": id,
            "nome": form.cleaned_data['nome'],
            "idade": form.cleaned_data['idade'],
            "cpf": form.cleaned_data['cpf'],
            "areaFormacao": form.cleaned_data['areaFormacao'],
        }
        client.action(schema, action, params=params)
        return redirect('listAvaliadores')


def deleteAvaliador(request, id):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs/")

    action = ["avaliadores", "delete"]
    params = {
        "id": id,
    }
    result = client.action(schema, action, params=params)
    return redirect('listAvaliadores')


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


def alterarPremio(request, id):
    premio = Premio.objects.get(id=id)
    form = PremioForm(instance=premio)

    if request.method == 'GET':
        return render(request, 'Premio/alterar_premio.html',
                      {'form': form, 'premio': premio})
    elif request.method == 'POST':
        form = PremioForm(request.POST, instance=premio)
        premio = form.save(commit=False)
        premio.nome = form.cleaned_data['nome']
        premio.idade = form.cleaned_data['idade']
        premio.cpf = form.cleaned_data['cpf']
        premio.areaFormacao = form.cleaned_data['areaFormacao']
        premio.save()

        # Initialize a client & load the schema document
        client = coreapi.Client()
        schema = client.get("http://127.0.0.1:8000/teste/docs")

        # Interact with the API endpoint
        action = ["autores", "update"]
        params = {
            "id": id,
            "nome": form.cleaned_data['nome'],
            "descricao": form.cleaned_data['descricao'],
            "ano": form.cleaned_data['ano'],
            "cronograma_fk": form.cleaned_data['cronograma_fk'].id,
        }
        client.action(schema, action, params=params)
        return redirect('listAvaliadores')


def deletePremio(request, id):
    client = coreapi.Client()
    schema = client.get("http://127.0.0.1:8000/teste/docs/")

    action = ["premios", "delete"]
    params = {
        "id": id,
    }
    result = client.action(schema, action, params=params)
    return redirect('listPremios')


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
