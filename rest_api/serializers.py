from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from reserva.models import Petshop, Reserva

class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):

   def __init__(self, **kwargs):
      # Corrigir a definição do serializer
      self.serializer = PetshopModelSerializer
      super().__init__(**kwargs)

   def use_pk_only_optimization(self):
      return False
   
   def to_representation(self, value):
      return self.serializer(value, context=self.context).data

class PetshopModelSerializer(ModelSerializer):
    # Defina o ModelSerializer para o modelo Petshop aqui (se ainda não existir)
    class Meta:
        model = Petshop
        fields = '__all__'

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )

    class Meta:
        model = Reserva
        fields = '__all__'
