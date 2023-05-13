from typing import Any, Optional
from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import Reserva

class Command(BaseCommand):
    help = 'Cria dados fake para testar a API de agendamento'

    def handle(self, *args, **options):
        pass