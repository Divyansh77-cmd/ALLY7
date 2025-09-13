from flask import Flask, request, jsonify, render_template
import os
import datetime

# Create the Flask application instance
app = Flask(__name__)

# --- Server-side Storage Setup ---
# Define the directory where complaints will be stored
COMPLAINTS_DIR = 'complaints'
# Create the directory if it doesn't exist
os.makedirs(COMPLAINTS_DIR, exist_ok=True)

# --- Routes and Logic ---

# Route to serve the main HTML page
@app.route('/')
def index():
    # This will now serve the separate index.html file
    return render_template('index.html')

# Route to handle the form submission
@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    try:
        data = request.json
        if not data or not all(key in data for key in ['platform', 'username', 'complaint']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Generate a unique filename using a timestamp
        timestamp = datetime.datetime.now().isoformat().replace(':', '-').replace('.', '_')
        filename = f"{timestamp}.txt"
        filepath = os.path.join(COMPLAINTS_DIR, filename)

        # Write the complaint data to the file
        with open(filepath, 'w') as f:
            f.write(f"Platform: {data['platform']}\n")
            f.write(f"Username: {data['username']}\n")
            f.write(f"Complaint: {data['complaint']}\n")
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
