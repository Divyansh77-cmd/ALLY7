from flask import Flask, request, jsonify, render_template
import os
import datetime
from werkzeug.utils import secure_filename


app = Flask(__name__)


COMPLAINTS_DIR = 'complaints'
UPLOADS_DIR = 'uploads'


os.makedirs(COMPLAINTS_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    try:
       
        platform = request.form.get('platform')
        username = request.form.get('username')
        complaint = request.form.get('complaint')
        
        
        if not all([platform, username, complaint]):
            return jsonify({'error': 'Missing required text fields'}), 400

        uploaded_filename = "No screenshot provided"
        
        if 'screenshot' in request.files:
            file = request.files['screenshot']
            if file and file.filename != '':
                
                original_filename = secure_filename(file.filename)
                
                timestamp = datetime.datetime.now().isoformat().replace(':', '-').replace('.', '_')
                uploaded_filename = f"{timestamp}_{original_filename}"
                filepath = os.path.join(UPLOADS_DIR, uploaded_filename)
                
               
                file.save(filepath)

        
        timestamp = datetime.datetime.now().isoformat().replace(':', '-').replace('.', '_')
        filename = f"{timestamp}.txt"
        filepath = os.path.join(COMPLAINTS_DIR, filename)

       
        with open(filepath, 'w') as f:
            f.write(f"Platform: {platform}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Complaint: {complaint}\n")
            f.write(f"Screenshot: {uploaded_filename}\n")
            f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")

        
        return jsonify({'message': 'Complaint submitted successfully'}), 200

    except Exception as e:
        print(f"Error handling complaint submission: {e}")
        return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    
    app.run(debug=True, port=5000)

