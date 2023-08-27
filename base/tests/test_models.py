from datetime import date, timedelta

import pytest
from model_bakery import baker

from reserva.models import Reserva

@pytest.fixture
<<<<<<< HEAD
def dados_validos():
=======
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
>>>>>>> 08a4069d7676b3617232000d5ebceac5b74e8caa
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
<<<<<<< HEAD
    return dados  




@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client):
    response = client.post('/reserva/criar/', dados_validos)

    assert response.status_code == 200
    assert 'Reserva realizada com sucesso' in str(response.content)


@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
    client.post('/reserva/criar/', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']
    assert reserva.nome_pet == dados_validos['nome_pet']
=======
    response = cliente.post('/reser')
>>>>>>> 08a4069d7676b3617232000d5ebceac5b74e8caa
