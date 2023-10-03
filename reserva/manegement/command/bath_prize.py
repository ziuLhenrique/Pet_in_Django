from django.core.management.base import BaseCommand

from reserva.models import Petshop

import random


class Command(BaseCommand):
    def list_Petshops(self):
        return Petshop.objects.all().values_list('pk', flat=True)
    
    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?'
            default=5,
            type=int,
            help='Sortear um cliente para receber um cupom para outro agendamento grátis'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_Petshops(),
            help='Petshop ID execute the contest'
        )

    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)

        return random.sample(banhos_list, quantidade)
    

    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write()
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados das pessoas e animais sorteados'
            )
        )
        self.stdout.write(
            self.style.HTTP_INFO(
                '=' * 35
            )
        )
        for reserva in reservas:
            self.stdout.write(
                f'Animal: {reserva.nome} - {reserva.email}'
            )
            self.stdout.write(
                f'Tutor: {reserva.nome} - {reserva.email}'
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    '=' * 35
                )
            )

    
    def handle(self, *args, **options):
        quantity = options['quantity']
        Petshop_id = options['petshop']

        petshop = Petshop.objects.get(pk=Petshop_id)
        reservas = petshop.reservas.all()
        banhos_escolhidos = self.escolher_reservas(reservas, quantity)
        
        self.stdout.write(
            self.style.SUCCESS('Sorteio concluido')
        )
        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos)
        
        for reserva in reservas:
            self.stdout.write(str(reserva))