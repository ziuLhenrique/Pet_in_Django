from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet #Adicionar viewset

from reserva.models import Reserva #Referenciar modelo
from rest_api.serializers import AgendamentoModelSerializer

from rest_framework.authentication import TokenAuthentication #Permitir que apenas usuários autenticados postem dados na API
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_api.serializers import Petshop, PetshopModelSerializer



class AgendamentoModelViewSet(ModelViewSet): #Criar classe
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer

    authentication_classes = [TokenAuthentication]#Permitir que apenas usuários autenticados postem dados na API
    permission_classes = [IsAuthenticatedOrReadOnly]


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET', 'POST', 'PUT'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    
    elif request.method == 'PUT':
        return Response({'Dolars': 'R$2.000,000,45' })
    
    else:
        return Response ({'Meu Saldo': 'R$5.110,200 To Rico $$$$$$!Ha!Ha!'})

