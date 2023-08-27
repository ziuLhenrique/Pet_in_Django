
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer
import datetime

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop =baker.make(Petshop)
    return{
        'nome': 'nome teste', 'email': 'email@email.com',
        'nome_pet': 'pett test', 'data': hoje, 'turno': 'manhã',
        'tamanho': 0, 'observacoes': '', 'petshop': petshop.pk,
    }

@pytest.mark.django_db
def test_todos_petshop():
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento')
    resposta = cliente.get('/api/petshop')
    assert resposta.data['results'] == 1