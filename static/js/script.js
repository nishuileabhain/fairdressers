$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.datepicker').datepicker(
      {
        format: "dd mmmm, yyyy",
        setDefaultDate: true,
        autoClose: true,
    }
    );  
  });
