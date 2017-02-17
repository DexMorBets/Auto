$(document).ready(function () {
    var page = $('#page').text();
    if (page == "1") {
        $(".mainpage").css('color','rgba(26, 188, 156, 0.81)')
    } else if (page == "2"){
        $(".servicespage").css('color','rgba(26, 188, 156, 0.81)')
    } else if (page == "3"){
        $(".pricepage").css('color','rgba(26, 188, 156, 0.81)')
    } else if (page == "4"){
        $(".aboutpage").css('color','rgba(26, 188, 156, 0.81)')
    } else if (page == "5"){
        $(".contactspage").css('color','rgba(26, 188, 156, 0.81)')
    };
});
