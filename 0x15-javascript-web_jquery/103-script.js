$(document).ready(function() {
    function fetchHello() {
        const language_code = $('#language_code').val()
        const urlApi = `https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}`

        $.get(urlApi, function(data) {
            $('#hello').text(data.hello)
        }).fail(function(){
            $('#hello').text('Error: could not fetch')
        })
    }

    $('#btn_translate').click(fetchHello)

    $('#language_code').keypress(function(e) {
        if (e.which === 13){
            fetchHello
        }
    })
})