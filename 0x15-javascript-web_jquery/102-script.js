$(document).ready(function() {
   $('#btn_translate').bind('click', function() {
    const language_code = $('#language_code').val()
    const urlApi = `https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}`

    $.get(urlApi, function(data) {
        $('#hello').text(data.hello)
    })
}) 
})
