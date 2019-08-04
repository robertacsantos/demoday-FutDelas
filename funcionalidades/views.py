
from django.shortcuts import render, redirect
from funcionalidades.models import Pessoa, Partida

# Create your views here.

    
def home(request):
    return render(request, 'home.html', {})
   
def index(request):
    #essa página vai cadastrar uma pessoa
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.senha = request.POST.get('senha')
        pessoa.idade = request.POST.get('idade')
        pessoa.save()
        contexto = {'msg': 'Parabéns, agora só colocar seu e-mail e senha'}
        return render(request, 'login.html', contexto)

    return render(request, 'index.html', contexto)


def sobre(request):
    #essa página vai listar as partidas e seus criadores
    partidas = Partida.objects.filter(ativo=True).all()
    contexto = {
        'partidas':partidas
    }
    return render(request, 'sobre.html', contexto)

def remover_partida(request, id):
    partida = Partida.objects.filter(id=id).first()
    if partida is not None:
        partida.ativo = False
        partida.save()
        return redirect('/sobre')
    return render(request, 'sobre.html')    

def login(request):
    # Essa página irá conferir se existe um usuário
    # cadastrado, se sim retonará para página sobre
    # se não, retornará para página de cadastro com
    # uma mensagem "Cadastre-se para criar uma partida"
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        pessoa = Pessoa.objects.filter(email=email_form, senha=senha_form).first()

        if pessoa is None:
            #mandar para página de cadastro
            contexto = {'msg': 'Cadastre-se para criar uma partida'}
            return render(request, 'index.html', contexto)
        else:
            #mandar para página de partidas
            contexto = {'pessoa': pessoa}
            return render(request, 'partidas.html', contexto)

    return render(request, 'login.html', {})

def cadastrar_partida(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        senha_pessoa = request.POST.get('senha')
        pessoa = Pessoa.objects.filter(email=email_pessoa, senha=senha_pessoa).first()
        if pessoa is not None:
            partida = Partida()
            partida.pessoa = pessoa
            partida.titulo = request.POST.get('titulo')
            partida.descricao = request.POST.get('descricao')
            partida.save()

            return redirect('/sobre') 

    return render(request, 'partida.html', {})
