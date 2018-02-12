$(document).ready(function(){

  function addClickHandlers(){
    $("button").click(getColor);
  }

  function getColor(){
    var color = $(this).attr('id');
    getData(color);
  }

  function getData(color){
    var url = 'http://localhost:5000/ninja/' + color
    $.get(url).done(function(data){
      var { image, name } = data;
      loadImage(image,name);
    });
  }

  function loadImage(image,name){
    var headline = $(".headline");
    var $image = $(".image img");
    if (name === "Notapril"){
      headline.text("That turrtle was not found!");
    }
    else {
      headline.text("You chose " + name + "!");
    }
    $image.attr("src",image).attr("alt",name);
  }

  addClickHandlers();
});
