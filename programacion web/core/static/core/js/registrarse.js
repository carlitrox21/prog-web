//VALIDO QUE EL USUARIO INGRESE UN CORREO VALIDO
$(document).ready(function () {
    $("#correo").on("input", function () {
        if (Fn.validarcorreo($("#correo").val())) {
            $("#correo").removeClass("error");
            $("#correo").addClass("ok");
            $("#errorcorreo").html("");
        } else {
            $("#correo").addClass("error");
            $("#correo").removeClass("ok");
            $("#errorcorreo").html("ingrese un correo valido");
        }
    });
    //VALIDO QUE INGRESE ALGO EN EL INPUT #NUM2
    $("#nombre").on("input", function () {
        if ($("#nombre").val() == "") {
            $("#nombre").addClass("error");
            $("#nombre").removeClass("ok");
            $("#errornom").html("debe ingresar un nombre");
        } else {
            $("#nombre").removeClass("error");
            $("#nombre").addClass("ok");
            $("#errornom").html("");
        }
    });
    $("#pass").on("input", function () {
        if ($("#pass").val() == "") {
            $("#pass").addClass("error");
            $("#pass").removeClass("ok");
            $("#errorpass").html("debe ingresar una contraseña");
        } else {
            $("#pass").removeClass("error");
            $("#pass").addClass("ok");
            $("#errorpass").html("");
        }
    });
    $("#conpass").on("input", function () {
        if ($("#conpass").val() ==$("#pass").val() ) {
            $("#conpass").addClass("ok");
            $("#conpass").removeClass("error");
            $("#errorconpass").html("");
        } else {
            $("#conpass").removeClass("ok");
            $("#conpass").addClass("error");
            $("#errorconpass").html("vuelva a ingresar su contraseña");
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
    if(($("#nombre").hasClass("ok"))){
        if (($("#correo").hasClass("ok"))){
            if (($("#pass").hasClass("ok"))){
                if (($("#conpass").hasClass("ok"))){
                    success = true;
}
}
}
}
return success;
}