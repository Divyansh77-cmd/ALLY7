from flask import Flask, request, jsonify, render_template
import os
import datetime
from werkzeug.utils import secure_filename

# Create the Flask application instance
app = Flask(__name__)

# --- Server-side Storage Setup ---
# Define the directories where complaints and uploads will be stored
COMPLAINTS_DIR = 'complaints'
UPLOADS_DIR = 'uploads'

# Create the directories if they don't exist
os.makedirs(COMPLAINTS_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

# --- Routes and Logic ---

# Route to serve the main HTML page
@app.route('/')
def index():
    # This will now serve the separate index.html file
    return render_template('index.html')

# Route to handle the form submission with file upload
@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    try:
        # Get text data from the form
        platform = request.form.get('platform')
        username = request.form.get('username')
        complaint = request.form.get('complaint')
        
        # Check for required text fields
        if not all([platform, username, complaint]):
            return jsonify({'error': 'Missing required text fields'}), 400

        uploaded_filename = "No screenshot provided"
        # Check if a file was uploaded
        if 'screenshot' in request.files:
            file = request.files['screenshot']
            if file and file.filename != '':
                # Secure the filename before saving to prevent directory traversal attacks
                original_filename = secure_filename(file.filename)
                # Generate a unique filename with a timestamp to avoid conflicts
                timestamp = datetime.datetime.now().isoformat().replace(':', '-').replace('.', '_')
                uploaded_filename = f"{timestamp}_{original_filename}"
                filepath = os.path.join(UPLOADS_DIR, uploaded_filename)
                
                # Save the file to the uploads directory
                file.save(filepath)

        # Generate a unique filename for the complaint text file
        timestamp = datetime.datetime.now().isoformat().replace(':', '-').replace('.', '_')
        filename = f"{timestamp}.txt"
        filepath = os.path.join(COMPLAINTS_DIR, filename)

        # Write the complaint data to the file, including the screenshot path
        with open(filepath, 'w') as f:
            f.write(f"Platform: {platform}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Complaint: {complaint}\n")
            f.write(f"Screenshot: {uploaded_filename}\n")
            f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")

        # Return a success message
        return jsonify({'message': 'Complaint submitted successfully'}), 200

    except Exception as e:
        print(f"Error handling complaint submission: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# To run the app, you would execute this file
if __name__ == '__main__':
    # You can change the port if needed. For the hackathon, 5000 is a good choice.
    app.run(debug=True, port=5000)
