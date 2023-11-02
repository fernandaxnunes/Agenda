from django.db import models

# Create your models here.
UFS = [
     ('SP', 'São Paulo'),
     ('RJ', 'Rio de Janeiro'),
     ('MG', 'Minas Gerais'),
     ('ES', 'Espírito Santo')
] 

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UFS)

    def __str__(self):
        return self.nome

class Agenda(models.Model):

    ESTADO_CIVIS = [
        ('S', 'Solteiro'), 
        ('C', 'Casado'), 
        ('D', 'Divorciado'), 
        ('V', 'Viúvo')
        ]
   
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name='Data de aniversário')
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=UFS, null=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIS, null=True)

    def __str__(self):
        return self.nome
    
class Telefone(models.Model):
    TIPOS_TELEFONE = [
        ('RES', 'Residencial'),
        ('COM', 'Comercial'),
        ('REC', 'Recado')
    ]
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=3, choices=TIPOS_TELEFONE)
    IsWhatsapp = models.BooleanField(verbose_name='Tem WhatsApp?')

    def __str__(self):
        return f'({self.ddd}) {self.numero}'


