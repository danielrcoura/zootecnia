# Sistema de Controle Zootécnico no IFPB Campus Sousa
Sistema de controle de animais dos tipos: bovinos, suínos, caprinos, ovinos, equinos,
aves e peixes. Pode-se ter o controle das coberturas, partos, ocorrências, coletas de leite,
perdas de animais, vendas de produtos entre outras atividades de rotina.


## Introdução
Visto a necessidade de um maior controle em relação aos animais de propriedades
agrícolas, o sistema de cadastramento fornece uma interface simples de interação com o usuário.  
Através dos dados obtidos o usuário pode ter uma noção maior dos problemas e tomar decisões
baseadas nos resultados fornecidos pelo software.

## Usage
```
pip3 install -r modules.txt
python3 manage.py makemigrations && python3 manage.py migrate
python3 manage.py runserver
```

## Página Admin
Para cadastrar animais é preciso antes cadastrar as raças, o sexo dos animais, as evoluções e os estados (ex. vivo, morto, vendido), isso pode ser feito na página de Admin.  
Para usar a página de Admin crie um super usuário com o comando abaixo:
```
python3 manage.py createsuperuser
```
A página pode ser acessada pelo link: [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
