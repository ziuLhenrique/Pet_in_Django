from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from reserva.models import Reserva
from rest_api.serializers import AgendamentoModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
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
