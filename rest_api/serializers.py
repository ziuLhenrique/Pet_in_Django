#from termios import CDSUSP   

from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

from reserva.models import Petshop, Reserva #Referenciar modelo


class PetshopModelSerializer(ModelSerializer):
   reservas = HyperlinkedRelatedField(
      many=True,
      read_only=True,
      view_name='api:reserva-detail'
   ) 


   class Meta:
      model = Petshop
      fields = '__all__'


class AgendamentoModelSerializer(ModelSerializer):
   petshop = PetshopModelSerializer(read_only=True)

   class Meta:
      model = Reserva
      fields = '__all__'



   