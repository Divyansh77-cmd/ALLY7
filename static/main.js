const form = document.getElementById('complaint-form');
const messageDiv = document.getElementById('message');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    try {
        const response = await fetch('/submit_complaint', {
            method: 'POST', 
            body: formData, 
        });

        
        if (response.ok) {
            
            messageDiv.innerHTML = '<span class="text-green-600 font-medium">Complaint submitted successfully! Thank you.</span>';
            form.reset(); 
        } else {
           
            const errorData = await response.json();
            messageDiv.innerHTML = `<span class="text-red-600 font-medium">Error: ${errorData.error}</span>`;
        }
    } catch (error) {
        
        messageDiv.innerHTML = `<span class="text-red-600 font-medium">An error occurred: ${error.message}</span>`;
        console.error('Error submitting complaint:', error);
    }
});
