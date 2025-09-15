// Get the form and message elements from the HTML document
const form = document.getElementById('complaint-form');
const messageDiv = document.getElementById('message');

// Add an event listener to the form for the 'submit' event
form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the default form submission behavior (page reload)

    // Create a FormData object from the form to easily get all input values and the file
    const formData = new FormData(form);

    try {
        // Use the Fetch API to send the form data to our backend
        const response = await fetch('/submit_complaint', {
            method: 'POST', // We are sending data, so use the POST method
            body: formData, // The browser will set the correct headers for multipart/form-data
        });

        // Check if the response from the server was successful
        if (response.ok) {
            // Display a success message to the user
            messageDiv.innerHTML = '<span class="text-green-600 font-medium">Complaint submitted successfully! Thank you.</span>';
            form.reset(); // Clear the form fields for a new submission
        } else {
            // If the response was not successful, parse the error message from the server
            const errorData = await response.json();
            messageDiv.innerHTML = `<span class="text-red-600 font-medium">Error: ${errorData.error}</span>`;
        }
    } catch (error) {
        // Handle any network-related errors
        messageDiv.innerHTML = `<span class="text-red-600 font-medium">An error occurred: ${error.message}</span>`;
        console.error('Error submitting complaint:', error);
    }
});
