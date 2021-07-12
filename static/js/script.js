/*jshint esversion: 6 */
const $ = window.$;

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
    $('body').Aplus();
    $('.tooltipped').tooltip();
    $('.modal').modal();
  });
  


 // code to send click data on content to python function to add to database
//thumbs up - adds 1 to current score in database and refreshes the dom and keeps location

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
    return ;
});
}


// thumbs down
//thumbs down - adds 1 to current score in database and refreshes the dom and keeps location


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
  return ;
});
}

// favourite article
//adds the details of content clicked to the favourites collection and creates quick link on profile
//Modal alerts user that added to favourites


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
  return ;
});
}

