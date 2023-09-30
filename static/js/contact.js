// EmailJS - Send email from contact form
// reference: https://martinezjf2.medium.com/how-to-setup-emailjs-33809350f0f8

document.getElementById("contactForm").addEventListener("submit", function(event) {
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

            // Submit the form
            document.getElementById("contactForm").submit();

            // Display success modal and hide the form
            document.getElementById("contactForm").style.display = "none";
            document.getElementById("successModal").style.display = "block";
        },
        function(error) {
            console.log('FAILED...', error);
        });
});