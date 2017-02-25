$(document).ready(function () {
    $('.menu-toolbar div').tap( function () {
        $(this).find('a').css('border-bottom', 'none');
    });
    $('.menu-toolbar-hidden div').tap( function () {
        $(this).find('a').css('border-bottom', 'none');
    });
    $('.menu-toolbar div').mouseenter( function () {
        $(this).find('a').css('border-bottom', '5px solid rgba(26, 188, 156, 0.81)');
    }).mouseleave(function () {
        $(this).find('a').css('border-bottom', 'none');
    })
    $('.menu-toolbar-hidden div').mouseenter( function () {
        $(this).find('a').css('border-bottom', '15px solid rgba(26, 188, 156, 0.81)');
    }).mouseleave(function () {
        $(this).find('a').css('border-bottom', 'none');
    })
})
