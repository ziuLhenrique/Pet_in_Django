
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer
import datetime

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop = baker.make(Petshop)
    return{
        'nome': 'nome teste', 'email': 'email@email.com',
        'nome_pet': 'pett test', 'data': hoje, 'turno': 'manhã',
        'tamanho': 0, 'observacoes': '', 'petshop': petshop.pk,
    }

@pytest.mark.django_db
def test_data_agendamento_invalida(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
    assert not serializer.is_valid()
