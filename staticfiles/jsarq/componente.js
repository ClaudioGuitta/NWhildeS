$(document).ready(function() {

    var baseUrl = 'http://barrabas.pythonanywhere.com/post_list';
    var filter = $('#filter');


    $(filter).change(function(){
       var filter = $(this).val();
       window.location.href = baseUrl + '?filter=' + filter;

    });
});