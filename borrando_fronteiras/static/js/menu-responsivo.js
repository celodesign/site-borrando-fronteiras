function menuShow(){
  let menuMobile = document.querySelector('.main-menu');
  let areaMenu = document.querySelector('#area-menu');
  if(menuMobile.classList.contains('actives')){
    menuMobile.classList.remove('actives');
    menuMobile.classList.remove('icon-open');
    areaMenu.classList.remove('open');
  }else{
    menuMobile.classList.add('actives');
    menuMobile.classList.add('icon-open');
    areaMenu.classList.add('open');
  }
}

function meuShowItens(){
  let itemMenu = document.querySelector('.item-menu');
  let menuMobile = document.querySelector('.main-menu');
  let areaMenu = document.querySelector('#area-menu');
  menuMobile.classList.remove('actives');
  menuMobile.classList.remove('icon-open');
  areaMenu.classList.remove('open');
}
