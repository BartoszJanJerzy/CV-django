//var burger = document.getElementById('burger');
//var menu = document.getElementById('menu');
//
//
//function ShowMenu(menu) {
//    menu.style.transition = '0.5s';
//    menu.style.display = 'flex';
//};
//
//burger.onclick = function(){
//    ShowMenu(menu);
//};

var shown = 0;

$('#burger').click(function(){
    if(shown === 0) {
        $('#menu').show(500);
        shown = 1;
    }
    else {
        $('#menu').hide(500);
        shown = 0;
    }
});