from django.db import models
from datetime import date

class Propriedade(models.Model):
	nome = models.CharField(max_length=255)
	proprietario = models.CharField(max_length=255)
	endereco = models.CharField(max_length=255)
	tamanho = models.IntegerField()
	observacoes = models.TextField(blank=True)
	def __str__(self):
		return self.nome

class Tipo(models.Model):
	tipo = models.CharField(max_length=255)
	def __str__(self):
		return self.tipo

class Sexo(models.Model):
	sexo = models.CharField(max_length=255)
	def __str__(self):
		return self.sexo

class Raca(models.Model):
	raca = models.CharField(max_length=255)
	def __str__(self):
		return self.raca

class Evolucao(models.Model):
	evolucao = models.CharField(max_length=255)
	def __str__(self):
		return self.evolucao

class Estado(models.Model):
	estado = models.CharField(max_length=255)

class AnimaisEnum(models.Model):
	numero = models.IntegerField()
	peso_nasc = models.FloatField()
	peso_desm = models.FloatField()
	pai = models.IntegerField()
	mae = models.IntegerField()
	propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
	tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
	sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
	raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
	evolucao = models.ForeignKey(Evolucao, on_delete=models.CASCADE)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.numero)

class AnimaisCol(models.Model):
	tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
	quantidade = models.IntegerField()
	raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
	propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.tipo)

class Atividade(models.Model):
	atividade = models.CharField(max_length=255)
	def __str__(self):
		return self.atividade

class OcorAtividade(models.Model):	
	atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
	data = models.DateField(default=date.today)
	def __str__(self):
		return str(self.atividade)

class Cobertura(models.Model):
	responsavel = models.CharField(max_length=255)
	reprodutor = models.IntegerField()
	matriz = models.IntegerField()
	data = models.DateField(default=date.today)
	def __str__(self):
		return str(self.reprodutor)

class Parto(models.Model):
	num_crias = models.IntegerField()
	reprodutor = models.IntegerField()
	matriz = models.ForeignKey(AnimaisEnum, on_delete=models.CASCADE)
	data = models.DateField(default=date.today)
	def __str__(self):
		return str(self.matriz)

class Ocorrencia(models.Model):
	animal = models.ForeignKey(AnimaisEnum, on_delete=models.CASCADE)
	ocorrencia = models.TextField()
	data = models.DateField(default=date.today)
	tratamento = models.TextField()
	custo = models.FloatField()
	def __str__(self):
		return str(self.animal)

class Perda(models.Model):
	animal = models.ForeignKey(AnimaisEnum, on_delete=models.CASCADE)
	causa = models.CharField(max_length=255)
	data = models.DateField(default=date.today)
	idade = models.IntegerField()
	def __str__(self):
		return str(self.animal)

class Leite(models.Model):
	manha = models.FloatField()
	tarde = models.FloatField()
	total = models.FloatField(blank=True)
	data = models.DateField(default=date.today)
	def __str__(self):
		return str(self.data)

class Produto(models.Model):
	produto = models.CharField(max_length=255)
	def __str__(self):
		return self.produto

class Venda(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	preco = models.FloatField()
	quantidade = models.FloatField()
	data = models.DateField(default=date.today)

