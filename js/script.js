
// adjust anchor point position & smooth rolling
$(function() {            
    $(".nav-sub a,area").on( "click" ,function() {
        var offsetTop = $(this).attr("href");
        var thisTop = $(offsetTop).offset().top;
        $('html, body').animate({
            scrollTop: thisTop - 100
        }, 500);
    });
});