from django.shortcuts import render, redirect
from django.urls import reverse
from lojaTaygra_app.models import  Produto, Contato, Desconto
from lojaTaygra_app.forms import ProdutoForm, ContatoForm, CadastroUsuario, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def home (request):
    produtos = Produto.objects.order_by('id')
    context = {'produtos': produtos, 'forms': LoginForm(), 'formcadastro': CadastroUsuario}
    return render(request, 'base.html', context)

def sobre (request):
    return render(request, 'sobre.html')

def contato (request):
    return render(request, 'contato.html')

def promocao (request):
    promocoes = Desconto.objects.order_by('data_cadastro')[:10]
    context = {'promocoes': promocoes}
    return render(request, 'desconto.html', context)

def add_produtos(request):
    if request.method == "GET":
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form':form}
    return render(request,'add_produtos.html',context)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():

            mensagem = Contato(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                assunto=form.cleaned_data['assunto'],
                mensagem=form.cleaned_data['mensagem']
            )
            mensagem.save()
            return redirect('home')  
    else:
        form = ContatoForm()
    
    return render(request, 'contato.html', {'form': form})

def formulario(request):
    return render (request, 'base.html', {'forms': LoginForm()})

def login (request):
    if request.method == 'POST':
        #fazer o login
       user = authenticate(username = request.POST.get('username'),
                        password =request.POST.get('password'))
       if user:
           auth_login(request, user)
    return HttpResponseRedirect(reverse('home'))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def cadastrouser(request):
    if request.method == 'POST':
        form = CadastroUsuario (request.POST)
        if form.is_valid():
            if request.POST.get('password') != request.POST.get('confirmacao'):
                form.add_error('password', 'As senhas devem ser iguais.')
            else:
                form = form.save(commit=False)
                form.password = make_password(form.password)
                form.save()
    return HttpResponseRedirect(reverse('home'))