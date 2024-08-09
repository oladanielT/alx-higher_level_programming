$('#add_item').bind('click', add)

function add(){
    var item = $("<li></li>").text('Item');

    $('.my_list').append(item);
}