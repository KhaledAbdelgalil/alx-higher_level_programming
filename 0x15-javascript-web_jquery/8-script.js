$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const listElement = $('UL#list_movies');
    for (let i = 0; i < data.results.length; i++) { listElement.append(`<li>${data.results[i].title}</li>`);}
});