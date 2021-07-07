window.onscroll = function(){
    if(document.documentElement.scrollTop > 100){
        document.querySelector('.boton-arriba-contenedor').classList.add('showu')
    
    }else{
        document.querySelector('.boton-arriba-contenedor').classList.remove('showu')
    }
}