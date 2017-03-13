function tipo(obj) {
	var e = document.getElementById("org");
	var itemSelecionado = e.options[e.selectedIndex].value;

    switch (itemSelecionado) {
    case 'enumerado':
	    document.getElementById('enumerado').style.display="block";
	    document.getElementById('coletivo').style.display="none";
	    document.getElementById("form_col").reset();
    break
    case 'coletivo':
	    document.getElementById('coletivo').style.display="block";
	    document.getElementById('enumerado').style.display="none";
	    document.getElementById("form_enum").reset();
    break
    }
}

function reseta(obj) {
	var x;
var r=confirm("Escolha um valor!");
if (r==true)
  {
  x="você pressionou OK!";
  }
else
  {
  x="Você pressionou Cancelar!";
  }
console.writeline(x);
}