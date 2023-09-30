// Delete Profile Modal

document.addEventListener('DOMContentLoaded', function () {
    // Get a reference to the "Delete Profile" button
    const deleteButton = document.getElementById('deleteProfileButton');
  
    // Add a click event listener to the button
    deleteButton.addEventListener('click', function () {
      // Show the modal when the button is clicked
      const deleteProfileModal = new bootstrap.Modal(document.getElementById('deleteProfileModal'));
      deleteProfileModal.show();
    });
  });