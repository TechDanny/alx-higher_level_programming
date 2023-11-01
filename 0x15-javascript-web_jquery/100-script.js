document.addEventListener('DOMContentLoaded', function () {
	const x = document.querySelector('header');
	if (x) {
		x.style.color = '#FF0000';
	} else {
		console.error('Header not found.');
	}
});
