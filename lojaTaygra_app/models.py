from django.db import models

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    descricao = models.TextField()
    subcategoria = models.ForeignKey("SubCategoria", on_delete=models.CASCADE)
    desconto = models.ForeignKey("Desconto", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nome

class Imagem (models.Model):
    nome = models.CharField(max_length=50)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.nome
    
class SubCategoria (models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nome
class Desconto (models.Model):
    valor = models.DecimalField(max_digits = 6, decimal_places = 2)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    
    def __str__ (self):
        return self.valor

class Contato (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.assunto