//VALIDO QUE EL USUARIO INGRESE UN CORREO VALIDO
$(document).ready(function () {
    $("#num1").on("input", function () {
        if (Fn.validarcorreo($("#num1").val())) {
            $("#num1").removeClass("error");
            $("#num1").addClass("ok");
            $("#errorcorreo").html("");
        } else {
            $("#num1").addClass("error");
            $("#num1").removeClass("ok");
            $("#errorcorreo").html("ingrese un correo valido");
        }
    });
    //VALIDO QUE INGRESE ALGO EN EL INPUT #NUM2
    $("#num2").on("input", function () {
        if ($("#num2").val() == "") {
            $("#num2").addClass("error");
            $("#num2").removeClass("ok");
            $("#errorpass").html("debe ingresar una contraseña");
        } else {
            $("#num2").removeClass("error");
            $("#num2").addClass("ok");
            $("#errorpass").html("");
            valpass = true
        }
    });

});

//funciones

var Fn = {
    validarcorreo: function (correo){
        re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
	if(re.test(correo)){
		return true;
    }
}
}


function validarFormulario(){
    let success = false;
    if(($("#num2").hasClass("ok"))){
        if (($("#num1").hasClass("ok"))){
            success = true;
    }
}
return success;
}



