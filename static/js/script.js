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

  // code to zoom in on content when click and zoom out when clicked again

  $('.content-container').click(function() {
    if ($(this).hasClass('active')){
      
      $('.content-container').removeClass('col s12 m8 offset-m2 l8 offset-l2 content-container active').addClass('col s12 l4 m6 content-container');
  }
  else {

       $('.content-container').removeClass('col s12 l4 m6 content-container').addClass('col s12 m8 offset-m2 l8 offset-l2 content-container active');
  }
    
  });

  


