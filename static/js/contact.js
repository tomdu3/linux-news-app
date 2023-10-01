// EmailJS - Send email from contact form
// reference: https://martinezjf2.medium.com/how-to-setup-emailjs-33809350f0f8

document.getElementById("emailForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    emailjs.send('gmail', 'rosie', {
        'from_name': name,
        'from_email': email,
        'project_request': message
    })
    .then(
        function(response) {
            console.log('SUCCESS!', response.status, response.text);

            // Display success modal
            const successModal = document.getElementById("successModal");
            successModal.classList.add("show");
            successModal.style.display = "block";
            successModal.setAttribute("aria-hidden", "false");

            // Hide the form
            const contactForm = document.getElementById("contactForm");
            contactForm.style.display = "none";
        }.function(error) {
            console.log('FAILED...', error);
        });
});