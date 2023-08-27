from django import forms
from reserva.models import Reserva

#ADICIONAR A BIB DE DATAS
from datetime import date

class ReservaForm(forms.ModelForm):
	
	#VALIDAR E IMPEDIR DE MARCAR DATAS NO PASSADO
	def clean_data(self):
		data = self.cleaned_data['data']
		hoje = date.today()
		if data < hoje:
			raise forms.ValidationError('Não é possível realizar uma reserva para o passado!')
		numReserva = Reserva.objects.filter(data=data).count()
		if numReserva >= 4:
			raise forms.ValidationError('Não há disponibilidade nesse dia, quatro reservas já foram feitas')
		return data
	
	class Meta:
		model = Reserva
		fields = [
			'nome', 'email', 'nome_pet', 'data', 'turno',
			'tamanho', 'observacoes'
		]