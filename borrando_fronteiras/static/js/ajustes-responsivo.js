function ajustesResponsivo(){
    let alturaDoSwiper = document.querySelector('.swiper');
    let alturaBorrando = alturaDoSwiper.clientHeight;
    //let itemBorrando = document.querySelector('.img-swiper'); 
    if(window.innerWidth == 1024 & window.innerHeight == 600){
      $('.img-swiper').css({'height': alturaBorrando});
    }
  };