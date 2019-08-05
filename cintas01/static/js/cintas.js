window.onload = function() {
	CargarDic();
};
var cintas =[];
var cintasBK =[];
var primero =true;
var resultado = [];


function CargarDic(){
	var tableReg = document.getElementById('LstCntsAlp');
	var cellsOfRow="";
	var cont = 0;
	if(primero == true)
	{
		for (var i = 1; i < tableReg.rows.length; i++)
		{
			cont +=1;
			cellsOfRow = tableReg.rows[i].getElementsByTagName('td');
			cintas.push({codigo:cellsOfRow[0].innerHTML,alojador:cellsOfRow[1].innerHTML,
							pasicion:cellsOfRow[2].innerHTML,cliente:cellsOfRow[3].innerHTML,tipo:cellsOfRow[4].innerHTML});
		}
		cintasBK=cintas;
		primero = false;
	}
	else
		cintas=cintasBK;
}




function Buscar() {
	var txt = document.getElementById('txt_buscado').value;
	Comparar(txt);
	BorrarAnt();
	InsertarNuv();
}




function Comparar(txt){
	resultado = [];
	var cont0=0;
	for (var i = cintas.length - 1; i >= 0; i--) {
		if(cintas[i].codigo.toUpperCase().indexOf(txt.toUpperCase()) > -1)
		{
			cont0 += 1;
			resultado.push(cintas[i]);
		}
	}
	$('#rpta').text(cont0);
}



function InsertarNuv() {
	var fila ='<tbody id="LstCntsAlp">';
	for (var i = resultado.length - 1; i >= 0; i--) 
	{
		fila +='<tr  style="font-size: 0.6em;"><td>'
		+resultado[i].codigo+"</td><td>"
		+resultado[i].alojador+"</td><td>"
		+resultado[i].posicion+'</td><td>'
		+resultado[i].cliente+"</td><td>"
		+resultado[i].tipo+"</td></tr>";						
	}
	fila +="</tbody>";
	$('#TablaCntsAlp').append(fila);
}

function BorrarAnt(){
	$('#LstCntsAlp').remove();
}


function VerificarCod() {
	var cad=document.getElementById('BarcodeCinta').value;
	if(cad.length > 5 ){
		VerificaDB(cad);
	}
}

function VerificaDB(cad){
	alert(">"+cad.length);
	
	var xhr = new XMLHttpRequest();
	var cad = "/c_ubicar/?cod="+cad;
	xhr.open('GET',cad,true); // sincrono o asincrono
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			console.log("retornó successfull-1");
			alert("retornó 4|200");
		}
	}
	xhr.send();
}