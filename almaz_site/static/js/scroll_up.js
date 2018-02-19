$(document).ready(function () {

    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.my_scroll_up').fadeIn();
        } else {
            $('.my_scroll_up').fadeOut();
        }
    });

    $('.my_scroll_up').click(function () {
        $("html, body").animate({scrollTop: 0}, 600);
        return false;
    });

});