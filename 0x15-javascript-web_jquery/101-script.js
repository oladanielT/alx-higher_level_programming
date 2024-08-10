$(document).ready(function(){
    $('#add_item').bind('click', function() {
        $('<li>Item</li>').appendTo('ul.my_list');
    });

    $('#remove_item').bind('click', function() {
        $('ul.my_list li:last-child').remove()
    })

    $('#clear_list').bind('click', function(){
        $('ul.my_list').empty();
    })
})