from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
   return render(request, 'inicio.html')

def contato(request):
   contexto = {
      'telefone': '(16) 99291-1234',
      'responsavel': 'Maria da Silva Pereira',
      'email': 'pettop@email.com',
   }
   return render(request, 'contato.html', contexto)