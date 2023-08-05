from datetime import date, timedelta

import pytest
from model_bakery import baker

from reserva.models import Reserva

@pytest.fixture
def reserva():
    data = date(2022, 8, 30)
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='tarde'
    )
    return reserva 




@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client):
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'João',
        'email': 'João@email.com',
        'nome_pet': 'Tom',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'O tom está bem fedorento'
    }
    response = cliente.post('/reser')