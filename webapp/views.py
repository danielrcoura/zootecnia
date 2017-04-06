from django.shortcuts import render, redirect

from .forms import (AnimaisEnumForm, 
	AnimaisColForm, 
	CoberturaForm, 
	PartoForm, 
	OcorrenciaForm, 
	LeiteForm, 
	VendaForm, 
	PropriedadeForm, 
	PerdaForm,
	OcorAtividadeForm,
)
from .models import(
	AnimaisEnum,
	AnimaisCol,
	Perda,
	Cobertura,
	Parto,
	Ocorrencia,
	Leite,
	Venda,
	OcorAtividade,
	Propriedade,
	)

def index(request): 
    return render(request, "principal/index.html")

def dashboard(request):
	return render(request, "principal/dashboard.html", {})

def enumerado(request):
	if request.method == "POST":
		form_enum = AnimaisEnumForm(request.POST)

		if form_enum.is_valid():
			post = form_enum.save(commit=False)
			post.save()
			form_enum = AnimaisEnumForm()
	else:
		form_enum = AnimaisEnumForm()
			
	context_enum ={
	'form_enum': form_enum,
	}

	return render(request, "principal/enumerado.html",context_enum)

def coletivo(request):
	if request.method == "POST":
		form_col = AnimaisColForm(request.POST)
		if form_col.is_valid():
			post = form_col.save(commit=False)
			post.save()
	else:
		form_col = AnimaisColForm()
		
	context_col ={
	'form_col': form_col,
	}
		
	return render(request, "principal/coletivo.html", context_col)

def perdas(request):
	if request.method == "POST":
		form_perda = PerdaForm(request.POST)
		if form_perda.is_valid():
			post = form_perda.save(commit=False)
			post.save()
	else:
		form_perda = PerdaForm()

	context ={'form_perda': form_perda}
	
	return render(request, "principal/perdas.html", context)

def cobertura(request):
	if request.method == "POST":
		form_cobertura = CoberturaForm(request.POST)
		if form_cobertura.is_valid():
			post = form_cobertura.save(commit=False)
			post.save()
	else:
		form_cobertura = CoberturaForm()

	context ={'form_cobertura': form_cobertura}

	return render(request, "principal/cobertura.html", context)

def parto(request):
	if request.method == "POST":
		form_parto = PartoForm(request.POST)
		if form_parto.is_valid():
			post = form_parto.save(commit=False)
			post.save()
	else:
		form_parto = PartoForm()

	context ={'form_parto': form_parto}

	return render(request, "principal/parto.html", context)

def ocorrencia(request):
	if request.method == "POST":
		form_ocorrencia = OcorrenciaForm(request.POST)
		if form_ocorrencia.is_valid():
			post = form_ocorrencia.save(commit=False)
			post.save()
	else:
		form_ocorrencia = OcorrenciaForm()

	context ={'form_ocorrencia': form_ocorrencia}

	return render(request, "principal/ocorrencia.html", context)

def leite(request):
	if request.method == "POST":
		form_leite = LeiteForm(request.POST)
		if form_leite.is_valid():
			post = form_leite.save(commit=False)
			post.save()
	else:
		form_leite = LeiteForm()

	context ={'form_leite': form_leite}

	return render(request, "principal/leite.html", context)

def venda(request):
	if request.method == "POST":
		form_venda = VendaForm(request.POST)
		if form_venda.is_valid():
			post = form_venda.save(commit=False)
			post.save()
	else:
		form_venda = VendaForm()

	context ={'form_venda': form_venda}

	return render(request, "principal/venda.html", context)

def atividade(request):
	if request.method == "POST":
		form_atividade = OcorAtividadeForm(request.POST)
		if form_atividade.is_valid():
			post = form_atividade.save(commit=False)
			post.save()
	else:
		form_atividade = OcorAtividadeForm()

	context ={'form_atividade': form_atividade}

	return render(request, "principal/atividade.html", context)

def propriedade(request):
	if request.method == "POST":
		form_propriedade = PropriedadeForm(request.POST)
		if form_propriedade.is_valid():
			post = form_propriedade.save(commit=False)
			post.save()
			form_propriedade = PropriedadeForm()
	else:
		form_propriedade = PropriedadeForm()

	context ={'form_propriedade': form_propriedade}

	return render(request, "principal/propriedade.html", context)

def list_animal_enum(request):
	animais_enum = AnimaisEnum.objects.all()
	
	context ={
	'animais_enum': animais_enum,
	}
	
	return render(request, "list/animal-enum.html", context)

def list_animal_col(request):
	animais_col = AnimaisCol.objects.all()
	
	context ={
	'animais_col': animais_col,
	}
	
	return render(request, "list/animal-col.html", context)

def list_perdas(request):
	list_perdas = Perda.objects.all()
	
	context ={
	'list_perdas': list_perdas,
	}
	
	return render(request, "list/perdas.html", context)

def list_cobertura(request):
	list_cobertura = Cobertura.objects.all()
	
	context ={
	'list_cobertura': list_cobertura,
	}
	
	return render(request, "list/cobertura.html", context)


def list_parto(request):
	list_parto = Parto.objects.all()
	
	context ={
	'list_parto': list_parto,
	}
	
	return render(request, "list/parto.html", context)

def list_ocorrencia(request):
	list_ocorrencia = Ocorrencia.objects.all()
	
	context ={
	'list_ocorrencia': list_ocorrencia,
	}
	
	return render(request, "list/ocorrencia.html", context)

def list_leite(request):
	list_leite = Leite.objects.all()
	
	context ={
	'list_leite': list_leite,
	}
	
	return render(request, "list/leite.html", context)

def list_venda(request):
	list_venda = Venda.objects.all()
	
	context ={
	'list_venda': list_venda,
	}
	
	return render(request, "list/venda.html", context)

def list_atividade(request):
	list_atividade = OcorAtividade.objects.all()
	
	context ={
	'list_atividade': list_atividade,
	}
	
	return render(request, "list/atividade.html", context)

def list_propriedade(request):
	elemento = request.GET.get('elemento')
	acao = request.GET.get('acao')
	print(elemento)
	if acao == 'editar':
		pass

	if acao == 'excluir':
		Propriedade.objects.filter(pk=elemento).delete()

	filtro = request.GET.get('filtro')
	pesquisa = request.GET.get('pesquisa')


	if pesquisa is not '' and filtro != None and filtro != 'filtro':
		if filtro == 'nome':
			query = Propriedade.objects.filter(nome__icontains=pesquisa)
		if filtro == 'proprietario':
			query = Propriedade.objects.filter(proprietario__icontains=pesquisa)
		if filtro == 'endereco':
			query = Propriedade.objects.filter(endereco__icontains=pesquisa)
		if filtro == 'tamanho':
			query = Propriedade.objects.filter(tamanho__icontains=pesquisa)
		context ={"query": query,
		'filtro': filtro,
		'pesquisa': pesquisa,
		}

	else:
		query = Propriedade.objects.all()
		filtro = 'filtro'
		pesquisa = ''
		context ={'query': query,
		'filtro': filtro,
		'pesquisa': pesquisa,
		}
		print("to no segundo if")

	return render(request, "list/propriedade.html", context)

def edit_animal_enum(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_animal_col(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_perdas(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_cobertura(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_parto(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_ocorrencia(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_leite(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_venda(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_atividade(request):
	query = Propriedade.objects.filter(pk=elemento)

	context = {'query': query}

	return render(request, "edit/propriedade.html", context)

def edit_propriedade(request):
	if request.method == "POST":
		teste = request.POST.get('nome')
		print(teste)
		form_propriedade = PropriedadeForm()
		return redirect('list_propriedade')
	else:
		form_propriedade = PropriedadeForm()
		context = {
		'form_propriedade': form_propriedade
		}
	elemento = request.GET.get('elemento')
	query = Propriedade.objects.filter(pk=elemento).get()

	print(query.proprietario)

	context = {'query': query,
		'form_propriedade': form_propriedade

	}

	return render(request, "edit/propriedade.html", context)
