from django.shortcuts import render
from .forms import (AnimaisEnumForm, 
	AnimaisColForm, 
	CoberturaForm, 
	PartoForm, 
	OcorrenciaForm, 
	LeiteForm, 
	VendaForm, 
	PropriedadeForm, 
	PerdaForm,
	TipoForm,
)

def index(request): 
    return render(request, "principal/index.html")

def dashboard(request):
	return render(request, "principal/dashboard.html", {})

def cadastro(request):
	if request.method == "POST":
		form_enum = AnimaisEnumForm(request.POST)
		if form_enum.is_valid():
			post = form_enum.save(commit=False)
			post.save()
	else:
		form_enum = AnimaisEnumForm()
		form_col = AnimaisColForm()
		form_tipo = TipoForm()
		
	context ={'form_enum': form_enum, 
	'form_col': form_col,
	'form_tipo': form_tipo,
	}

	return render(request, "principal/cadastro.html", context)

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
	return render(request, "principal/atividade.html", {})

def propriedade(request):
	if request.method == "POST":
		form_propriedade = PropriedadeForm(request.POST)
		if form_propriedade.is_valid():
			post = form_propriedade.save(commit=False)
			post.save()
	else:
		form_propriedade = PropriedadeForm()

	context ={'form_propriedade': form_propriedade}

	return render(request, "principal/propriedade.html", context)