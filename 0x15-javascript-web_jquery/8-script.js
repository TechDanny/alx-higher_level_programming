$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
	$('DIV#character').html(data['name']);
});
