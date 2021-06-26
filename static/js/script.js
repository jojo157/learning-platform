$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
    M.textareaAutoResize($('#body'));

  });
  
  $('.refresh').click(function() {
    setTimeout(function(){ location.reload()},1000);
  });

