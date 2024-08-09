$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, data_status){
    data.results.forEach(movie => {
        $('#list_movies').append($('<li></li>').text(movie.title)) 
    });
})