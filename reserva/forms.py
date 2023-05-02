from datetime import date
from django import forms
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        num_reservas = Reserva.objects.filter(data=data).count()
        if num_reservas >= 4:
            raise forms.ValidationError('Já existem 4 reservas para este dia.')
        if data < hoje:
            raise forms.ValidationError('Não é possível fazer uma reserva para o passado!')
        return data

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'observacoes'
        ]


