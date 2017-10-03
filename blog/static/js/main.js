$(document).ready(function(){
    var onMenu = false;
    $('.sidebar').hide();
    
    $('.sidebar--button').click(function(){
        
        $('.sidebar').slideToggle(1000, function(){
            // Ajuste do painel de postagens
            if(onMenu){
                $('.main').css({'margin-left': '5%'});
                $('.sidebar--button').css({'margin-left': '14px'});
            }else{
                $('.main').css({'margin-left': '15%'});
                $('.sidebar--button').css({'margin-left': '75px'});
            }
            onMenu = !onMenu;
        });
    });
});