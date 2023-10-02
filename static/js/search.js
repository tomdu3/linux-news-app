// Search Page Functions

// Function to clear the search field
document.addEventListener('DOMContentLoaded', function() {
	const inputField = document.querySelector('#input-search');
	const clearSearch = document.getElementById('clearSearch');

	if (inputField.value.length > 0) {
		clearSearch.style.visibility = 'visible';
	} else {
		clearSearch.style.visibility = 'hidden';
	}
});


document.querySelector('#input-search').addEventListener('keyup', function() {
	const clearSearch = document.getElementById('clearSearch');

	if (this.value.length > 0) {
		clearSearch.style.visibility = 'visible';
	} else {
		clearSearch.style.visibility = 'hidden';
	}
});

// If the search field is empty, the Clear button appears/disappears

document.querySelector('#clearSearch').addEventListener('click', function() {
	document.querySelector('#input-search').value = '';
	this.style.visibility = 'hidden';
});