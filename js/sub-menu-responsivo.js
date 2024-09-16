function menuShow(){
    let subMenu = document.querySelector('.sub-menu');
    if (subMenu.classList.contains('open')){
        subMenu.classList.remove('open');
        document.querySelector('.sub-menu').classList.add('open-second');
        document.querySelector('.icon').src = 'imagens/icon-sub-menu.svg';
    }else{
        subMenu.classList.add('open');
        document.querySelector('.sub-menu').classList.remove('open-second');
        document.querySelector('.icon').src = 'imagens/icon-sub-menu-fechar.svg';
    }
    console.log(subMenu);
}