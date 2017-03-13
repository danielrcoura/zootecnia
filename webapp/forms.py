from django import forms
from .models import AnimaisEnum, AnimaisCol, Cobertura, Parto, Ocorrencia, Leite, Venda, Propriedade, Perda

class AnimaisEnumForm(forms.ModelForm):

    class Meta:
        model = AnimaisEnum
        fields = ('numero', 'pai', 'mae', 'peso_nasc', 'peso_desm', 'propriedade', 'sexo', 'raca', 'evolucao', 'estado')

class AnimaisColForm(forms.ModelForm):
	
	class Meta:
		model = AnimaisCol
		fields = ('raca', 'quantidade', 'propriedade')
			
class CoberturaForm(forms.ModelForm):
	
	class Meta:
		model = Cobertura
		fields = ('responsavel', 'reprodutor', 'matriz', 'data')

class PartoForm(forms.ModelForm):
	
	class Meta:
		model = Parto
		fields = ('num_crias', 'reprodutor', 'matriz', 'data')

class OcorrenciaForm(forms.ModelForm):
	
	class Meta:
		model = Ocorrencia
		fields = ('animal', 'custo', 'data', 'ocorrencia', 'tratamento')

class LeiteForm(forms.ModelForm):
	
	class Meta:
		model = Leite
		fields = ('manha', 'tarde', 'total', 'data')

class VendaForm(forms.ModelForm):
	
	class Meta:
		model = Venda
		fields = ('produto', 'preco', 'quantidade', 'data')

class PropriedadeForm(forms.ModelForm):
	
	class Meta:
		model = Propriedade
		fields = ('nome', 'proprietario', 'endereco', 'tamanho', 'observacoes')

class PerdaForm(forms.ModelForm):
	
	class Meta:
		model = Perda
		fields = ('animal', 'idade', 'causa', 'data')

