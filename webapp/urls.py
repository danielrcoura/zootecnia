from django.conf.urls import url
from .views import (
	index,
	dashboard,
	cadastro,
	perdas,
	cobertura,
	parto,
	ocorrencia,
	leite,
	venda,
	atividade,
	propriedade,
	)

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^cadastro/$', cadastro, name="cadastro"),
    url(r'^perdas/$', perdas, name="perdas"),
    url(r'^cobertura/$', cobertura, name="cobertura"),
    url(r'^parto/$', parto, name="parto"),
	url(r'^ocorrencia/$', ocorrencia, name="ocorrencia"),
	url(r'^leite/$', leite, name="leite"),
	url(r'^venda/$', venda, name="venda"),
	url(r'^atividade/$', atividade, name="atividade"),
	url(r'^propriedade/$', propriedade, name="propriedade"),

]
