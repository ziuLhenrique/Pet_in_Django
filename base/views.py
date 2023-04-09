from django.shortcuts import render
from base.forms import ContatoForm


def inicio(request):
   return render(request, 'inicio.html')

def contato(request):
   sucesso = False
   if request.method == 'GET':
      form = ContatoForm()
   else:
      form = ContatoForm(request.POST)
      if form.is_valid():
         sucesso = True
   contexto = {
      'telefone': '(16) 99291-1234',
      'responsavel': 'Maria da Silva Pereira',
      'form': form,
      'sucesso': sucesso
   }
   return render(request, 'contato.html', contexto)