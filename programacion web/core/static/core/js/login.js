$('#btnIngreso').on('click', function(e){

    e.preventDefault();

    nombreUsuario = $('#nombreUsuario');
    contrasena = $('#contrasena');
    

    // if(validaFormulario()){
    //     alertify.alert('Inicio de sesión exitoso', `Bienvenido "${nombreUsuario.val()}"`);
    //     setTimeout(() => {
    //         window.location.href = '../';
    //     }, 2000);
    // }

});