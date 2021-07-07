$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
    $('body').Aplus();
    $('.tooltipped').tooltip();
    $('.modal').modal();
  });
  
 
//Library (home) page interactions
  // code to zoom in on content when click and zoom out when clicked again

  $('i.fas.fa-expand-alt').click(function() {
    if ($(this).hasClass('active')){
      $('.content-container').removeClass('col s12 m8 offset-m2 l8 offset-l2 content-container').addClass('col s12 l4 m6 content-container'); 
      $(this).removeClass('active');
      $(this)[0].scrollIntoView(0, -40);
      
    }
  else {
       $(this).addClass('active');
       $('.content-container').removeClass('col s12 l4 m6 content-container').addClass('col s12 m8 offset-m2 l8 offset-l2 content-container');
       $(this)[0].scrollIntoView(0, -40);
  }
      });

 // code to send click data on content to python function to add to database
//thumbs up - adds 1 to current score in databse and refreshes  the dom and keeps location

$('.score_up').click(function(event) {
    event.stopPropagation();
    event.stopImmediatePropagation();
    try{
      score_up(this.id);
    }
    finally{
      var value = parseInt($(this).text());
      value = value + 1;
      $(this).find("span").text(value);
    }   
}); 


function score_up(id){
  var articleV = id;

  var data = {
    article : articleV
  };

  fetch(`${window.origin}/home/score_up/`, {
    method:"POST",
    credentials: "include",
    body: JSON.stringify(data),
    cache: "no-cache",
    headers: new Headers({"content-type": "application/json"})
  })
.then(function(response){
    return 200;
})
}


// thumbs down

$('.score_down').click(function(event) {
  event.stopPropagation();
  event.stopImmediatePropagation();
  try{
    score_down(this.id);
  }
  finally{
    var value = parseInt($(this).text());
      value = value + 1;
      $(this).find("span").text(value);
  }   
}); 


function score_down(id){
var articleV = id;

var data = {
  article : articleV
};

fetch(`${window.origin}/home/score_down/`, {
  method:"POST",
  credentials: "include",
  body: JSON.stringify(data),
  cache: "no-cache",
  headers: new Headers({"content-type": "application/json"})
})
.then(function(response){
  return 200;
})
}

// favourite article


$('.fav_content').click(function(event) {
  event.stopPropagation();
  event.stopImmediatePropagation();
  try{
    fav_content(this.id);
  }
  finally{
    $('.modal').modal('open');
  }   
}); 


function fav_content(id){
var articleV = id;

var data = {
  article : articleV
};

fetch(`${window.origin}/fav_content/`, {
  method:"POST",
  credentials: "include",
  body: JSON.stringify(data),
  cache: "no-cache",
  headers: new Headers({"content-type": "application/json"})
})
.then(function(response){
  return 200;
})
}