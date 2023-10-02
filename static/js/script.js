// GLOBAL FUNCTIONS

// Fade out the alert after 3 seconds

function fadeOutAlert() {
	const alerts = document.querySelectorAll('.alert');

	alerts.forEach((alert) => {
		setTimeout(() => {
			alert.style.transition = 'opacity 1s';
			alert.style.opacity = '0';

			setTimeout(() => {
				alert.remove();
			}, 1000); // Remove the alert after fade out
		}, 3000); // Delay for 3 seconds before starting to fade out
	});
}

window.addEventListener('load', fadeOutAlert);


// Adjust the footer position to make it stick to the bottom of the page when the content is smaller than the viewport

function adjustFooter() {
	const body = document.body;
	const html = document.documentElement;
	const footer = document.querySelector('footer');

	const windowHeight = window.innerHeight;
	const bodyHeight = Math.max(
		body.scrollHeight,
		body.offsetHeight,
		html.clientHeight,
		html.scrollHeight,
		html.offsetHeight
	);

	if (windowHeight >= bodyHeight) {
		// Content is smaller than the viewport
		footer.classList.add('fixed-bottom');
	} else {
		// Content is larger than the viewport
		footer.classList.remove('fixed-bottom');
	}
}

// Call the function when the page loads and on window resize
window.addEventListener('load', adjustFooter);
window.addEventListener('resize', adjustFooter);