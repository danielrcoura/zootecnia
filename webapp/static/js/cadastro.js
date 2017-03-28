document.getElementById("id_tipo_cadastro_0").onchage = function() {
   window.location.href = "/cadastro/enumerado"; 
};

document.getElementById("id_tipo_cadastro_1").onchage = function() {
   window.location.href = "/cadastro/coletivo"; 
};

function teste(obj) {
    var e = document.getElementByName("tipo_cadastro");
    var itemSelecionado = e.options[e.selectedIndex].value;


    switch (itemSelecionado) {
    case 'Enumerado':
        window.location.href = "/cadastro/enumerado";
    break
    
    case 'Coletivo':
        window.location.href = "/cadastro/coletivo";
    break

    }
}

//     window.onload = function(){
//             document.getElementById('id_tipo').value = itemSelecionado;
// }



// document.getElementById('coletivo').style.display="block";
