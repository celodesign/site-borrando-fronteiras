$(document).ready(function(){
  $(".main-menu").click(function(){
    const larguraTela = screen.width;
    if(!$(this).hasClass("actives")){
      $("#aside").addClass("main-menu-open");
      $(this).addClass("actives");
      $(".main-menu").css("right", "71%")  
      if(larguraTela == 320){
        $(".main-menu").css("right", "67%");
      }else if(larguraTela == 768) {
        $(".main-menu").css("right", "61%");
      }else{
        $(".main-menu").css("right", "71%");
      }  
    }else{
      $("#aside").removeClass("main-menu-open");
      $(this).removeClass("actives");   
      if(larguraTela == 320){
        $(".main-menu").css("right", "190%");
      }else if(larguraTela == 768) {
        $(".main-menu").css("right", "115%");
      }else{
        $(".main-menu").css("right", "165%");
      }
    }
    console.log(larguraTela);
  });
  
});

$(document).ready(function(){
  $(".act-start").click(function(){
    const larguraTela = screen.width;
    if(!$(".main-menu").hasClass("act")){
        $("#aside").addClass("main-menu-open");
        $(".main-menu").addClass("actives");
        $(".main-menu").css("right", "71%");
        if(larguraTela == 320){
        $(".main-menu").css("right", "67%");
        }else if(larguraTela == 768) {
          $(".main-menu").css("right", "115%");
        }else{
          $(".main-menu").css("right", "71%");
        }  
    }else{
        $("#aside").removeClass("main-menu-open");
        $(".main-menu").removeClass("actives");
        $(".main-menu").css("right", "165%")
        if(larguraTela == 320){
        $(".main-menu").css("right", "190%");
        }else if(larguraTela == 768) {
          $(".main-menu").css("right", "115%");
        }else{
          $(".main-menu").css("right", "165%");
        }
    }
    console.log(larguraTela);
  });
  
});