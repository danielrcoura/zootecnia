function teste(obj) {
	var e = document.getElementById("id_tipo");
	var itemSelecionado = e.options[e.selectedIndex].value;


    switch (itemSelecionado) {
    case 'Bovino':
    case 'Ovino':
    case 'Caprino':
    case 'Suino':
	    document.getElementById('enumerado').style.display="block";
	    document.getElementById('coletivo').style.display="none";
    break
    
    case 'Equino':
    case 'Ave':
    case 'Peixe':
		document.getElementById('coletivo').style.display="block";
	    document.getElementById('enumerado').style.display="none";
    break

	case '---------':
    	document.getElementById('enumerado').style.display="none";
    	document.getElementById('coletivo').style.display="none";
    break
    }
}

	    