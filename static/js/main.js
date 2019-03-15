$(document).ready(function() {
    $( ".card-select" ).hover( function() {
        $(this).addClass('shadow').css('cursor', 'pointer');
        }, function() {
        $(this).removeClass('shadow');
        }
    );
    $(".card-select").click(function() {
        window.location = $(this).find("a").attr("href");
        return false;
    });
});

$(document).ready(function() {
    // run test on initial page load
    checkSize();

    // run test on resize of the window
    $(window).resize(checkSize);
});

//Function to the css rule
function checkSize(){
    if ($(".mobileSizing").css("float") == "none" ){
        $(".display-1").removeClass("display-1").addClass("display-4")
        $(".display-3").removeClass("display-3").addClass("display-5")
    }
    else {
        $(".display-4").removeClass("display-4").addClass("display-1")
        $(".display-5").removeClass("display-5").addClass("display-3")
    }
}