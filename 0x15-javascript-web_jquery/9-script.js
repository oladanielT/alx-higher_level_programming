$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data, data_status){
    $('#hello').text(data.hello)
})