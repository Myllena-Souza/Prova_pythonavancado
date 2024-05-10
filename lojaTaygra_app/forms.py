from django import forms
from lojaTaygra_app.models import Produto, Contato, Imagem
from django.forms.widgets import *
from django.contrib.auth.models import User

class ProdutoForm (forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao']
        labels = {'preco':"Preço"}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Nome do produto',
            'class' : 'form-control'}
        )
        self.fields['preco'].widget.attrs.update(
            {'placeholder':'Preço',
            'class' : 'form-control'}
        )
        self.fields['descricao'].widget.attrs.update(
            {'placeholder':'Descrição',
            'class' : 'form-control'}
        )

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['nome']     
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Nome da imagem',
            'class' : 'form-control'}
        )
        
class ContatoForm(forms.Form):
    class Meta: 
        model= Contato
        fields = ['nome','email','assunto','mensagem']

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Nome',
            'class' : 'form-control'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder':'E-mail',
            'class' : 'form-control'}
        )
        self.fields['assunto'].widget.attrs.update(
            {'placeholder':'Assunto',
            'class' : 'form-control'}
        )
        self.fields['mensagem'].widget.attrs.update(
            {'placeholder':'Mensagem',
            'class' : 'form-control'}
        )
        
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto', max_length=255)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

class LoginForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password']
        widgets = {'password': PasswordInput()}
            
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'placeholder':'Nome Usuário',
        'class' : 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
        {'placeholder':'Senha',
        'class' : 'form-control'}
        )
        
class CadastroUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'email': EmailInput(), 'password':PasswordInput()}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
        {'placeholder':'Nome',
        'class' : 'form-control'}
        )
        self.fields['last_name'].widget.attrs.update(
        {'placeholder':'Sobrenome',
        'class' : 'form-control'}
        )
        self.fields['username'].widget.attrs.update(
        {'placeholder':'Usuário',
        'class' : 'form-control'}
        )
        self.fields['email'].widget.attrs.update(
        {'placeholder':'E-mail',
        'class' : 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
        {'placeholder':'Senha',
        'class' : 'form-control'}
        )