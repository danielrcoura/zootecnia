from django import forms
from .models import (AnimaisEnum, 
	AnimaisCol,
	Cobertura,
	Parto,
	Ocorrencia,
	Leite,
	Venda,
	Propriedade,
	Perda,
	OcorAtividade,
	)

class AnimaisEnumForm(forms.ModelForm):

    class Meta:
        model = AnimaisEnum
        fields = ('tipo', 'numero', 'pai', 'mae', 'peso_nasc', 'peso_desm', 'propriedade', 'sexo', 'raca', 'evolucao', 'estado')

class AnimaisColForm(forms.ModelForm):
	
	class Meta:
		model = AnimaisCol
		fields = ('tipo', 'raca', 'quantidade', 'propriedade')
			
class CoberturaForm(forms.ModelForm):
	
	class Meta:
		model = Cobertura
		fields = ('reprodutor', 'matriz', 'data', 'responsavel')

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
		widgets = {
            'observacoes': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }

class PerdaForm(forms.ModelForm):
	
	class Meta:
		model = Perda
		fields = ('animal', 'idade', 'causa', 'data')

# class TipoForm(forms.Form):
#     FILTER_CHOICES = (
#         ('Enumerado', 'Enumerado'),
#         ('Coletivo', 'Coletivo'),

#     )

#     tipo_cadastro = forms.ChoiceField(choices = FILTER_CHOICES, widget=forms.RadioSelect(attrs={"onchange": "teste(this)"}))

class OcorAtividadeForm(forms.ModelForm):
	
	class Meta:
		model = OcorAtividade
		fields = ('atividade', 'data')