$(function(){
    var $username = $('#username');
    var $password = $('#password');
    $('#loginBtn').on('click',function(){

        var login ={
            username : $username.val(),
            password : $password.val(),
        };
        $.ajax({
            type:'POST',
            url:'https://psiquelife.com.br:8000/sistemaPsicologo/login/',
            data: login,
            success : function(user){
                localStorage.setItem('token', user.token);
                localStorage.setItem('tipoUsuario', user.tipoUsuario);
                localStorage.setItem('username', user.username);
                localStorage.setItem('userId', user.id);
                window.location.replace("index.html");

            },
            error : function(mensagem){
                alert(mensagem.responseText);
            }
        });
    });
});