$(document).ready(function () {
    $('.menu-toolbar div').tap( function () {
        $(this).find('a').css({'border-bottom':'5px solid rgba(26, 188, 156, 0.81)', 'color':'rgba(26, 188, 156, 0.81)'});
    });
    $('.menu-toolbar-hidden div').tap( function () {
        $(this).find('a').css({'border-bottom':'5px solid rgba(26, 188, 156, 0.81)', 'color':'rgba(26, 188, 156, 0.81)'});
    });
    $('.menu-toolbar div').mouseenter( function () {
        $(this).find('a').css({'border-bottom' : '5px solid rgba(26, 188, 156, 0.81)', 'color' : 'rgba(26, 188, 156, 0.81)'});
    }).mouseleave(function () {
        $(this).find('a').css({'border-bottom':'none', 'color':'black'});
    })
    $('.menu-toolbar-hidden div').mouseenter( function () {
        $(this).find('a').css({'border-bottom':'5px solid rgba(26, 188, 156, 0.81)', 'color':'rgba(26, 188, 156, 0.81)'});
    }).mouseleave(function () {
        $(this).find('a').css({'border-bottom':'none', 'color':'black'});
    })
})
