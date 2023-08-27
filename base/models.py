from django.db import models

# Create your models here.
from django.db import models
class Contato(models.Model):
	nome = models.CharField(max_length=50)
	email = models.EmailField(max_length=75)
	mensagem = models.TextField()
	data = models.DateTimeField(auto_now_add=True)
	lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)
	
#DEFINIR NOMES
	def __str__(self):
		return f'{self.nome}[{self.email}]'
	class Meta:
		verbose_name = 'Formulário de Contato'
		verbose_name_plural = 'Formulários de Contatos'
		ordering = ['-data']