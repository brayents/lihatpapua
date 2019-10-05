$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    if(scroll < 100){
        $('.fixed-top').css('background', 'transparent');
    } else{
        $('.fixed-top').css('background', 'rgba(0, 0, 0, 1)');
    }
});
