from django.contrib import admin

# Register your models here.

#PRECISA IMPORTAR O MODELS
from base.models import Contato

#PRECISA IMPORTAR MESSAGES
from django.contrib import messages


#DEFINIR FUNCAO PARA A ACAO DE ADMIN
@admin.action(description='Marcar Formulário(s) de Contato como lido(s)')
def marcar_como_lido (modeladmin, request, queryset):
	queryset.update(lido=True)
	modeladmin.message_user(request, 'Formulário(s) de Contato marcado(s) como lido(s)', messages.SUCCESS)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
	#ADICIONAR LIDO NO DISPLAY
	list_display = ['nome', 'email', 'lido', 'data']
	search_fields = ['nome', 'email']
	#ADICIONAR LIDO EM ADMIN
	list_filter = ['data', 'lido']
	#INDICAR ACAO PERMITIDA
	actions = [marcar_como_lido]