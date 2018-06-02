$(window).scroll(function() {
     if ($(document).scrollTop() > 100) {
       $('nav').addClass('shrink');
       $(".fade-text").fadeOut(1500);
       $(".head-letters").addClass('shrink');
     } else {
       $('nav').removeClass('shrink');
       $('.fade-text').fadeIn(1500);
       $(".head-letters").removeClass('shrink')
     }
});
