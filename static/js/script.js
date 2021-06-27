$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
    M.textareaAutoResize($('#body'));
    $('body').Aplus();

  });
  
  $('.refresh').click(function() {
    setTimeout(function(){ location.reload()},1000);
  });

