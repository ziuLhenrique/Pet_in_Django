#from django.shortcuts import render
#from rest_framework.decorators import api_view
#from rest_framework.response import Response


 

from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

from .serializers import AgendamentoModelSerializer
from reserva.models import  Petshop

from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

from .models import Petshop




class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api: reserva-detail'

    )

    class Meta: 
        model = Petshop
        fields = '__all__'




'''
@api_view(['GET', 'POST', 'PUT'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    
    elif request.method == 'PUT':
        return Response({'Dolars': 'R$2.000,000,45' })
    
    else:
        return Response ({'Meu Saldo': 'R$5.110,200 To Rico $$$$$$!Ha!Ha!'})
'''
