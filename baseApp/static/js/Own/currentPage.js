$(document).ready(function () {
    var page = $('#page').text();
    if (page == "1") {
        $(".mainpage").css('color','rgba(151, 227, 234, 0.9)')
    } else if (page == "2"){
        $(".servicespage").css('color','rgba(151, 227, 234, 0.9)')
    } else if (page == "3"){
        $(".pricepage").css('color','rgba(151, 227, 234, 0.9)')
    } else if (page == "4"){
        $(".aboutpage").css('color','rgba(151, 227, 234, 0.9)')
    } else if (page == "5"){
        $(".contactpage").css('color','rgba(151, 227, 234, 0.9)')
    };
});