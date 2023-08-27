import datetime
from rest_framework.serializers import(
    ModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)

from reserva.models import Petshop, Reserva

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )

def validate_data(self, value):
    hoje = datetime.date.today()
    if value < hoje:
        raise ValidationError('Não é possivel realizar um agendamento para o passado!')
    return value

class Meta:
    model = Reserva
    fields = '__all__'