Ally: An Online Harassment Reporting Tool
Project Overview
Ally is a web-based platform designed to combat online harassment by providing a simple and secure way for users to report incidents. The application captures key details about an incident, including the platform, harasser's username, and a detailed description, with the optional ability to upload a supporting screenshot. All submitted complaints are saved on the server for later review and analysis.

Our goal for this hackathon project was to create a functional prototype that demonstrates the core features of a community-driven reporting system.

Features
Intuitive Frontend: A clean, modern, and responsive user interface inspired by professional websites like bark.com.

Secure Reporting: A form that captures essential information about the harassment incident.

Screenshot Upload: The ability to submit a screenshot as evidence.

Server-Side Storage: All complaints are securely saved as text files on the server's file system, with screenshots stored in a separate directory.

Lightweight Backend: Built using Python and the Flask micro-framework, making it easy to set up and run.

Technology Stack
Frontend
HTML5: For the page structure.

Tailwind CSS: For all styling, ensuring a consistent and responsive design without external CSS files.

Vanilla JavaScript: For form handling and communication with the backend.

Backend
Python: The core programming language.

Flask: A lightweight and flexible micro-framework for the web server.

Getting Started
Follow these steps to get the project up and running on your local machine.

Prerequisites
You will need the following installed on your system:

Python 3.x

pip (Python package installer)

Installation
Clone the Repository: (If applicable)

Install Dependencies:

pip install Flask
pip install Werkzeug

Set up the Directory Structure:
Ensure your project directory is organized as follows:

your_project/
|-- app.py
|-- templates/
|   |-- index.html
|-- static/
|   |-- main.js
|-- complaints/ (will be created automatically)
|-- uploads/ (will be created automatically)

Running the Application
Navigate to the root directory of your project in your terminal.

Run the Flask application:

python app.py

Open your web browser and go to http://127.0.0.1:5000 to view the application.

How It Works
The frontend index.html page displays the complaint form.

The main.js file handles the form submission, gathering the form data (including the optional screenshot).

It sends this data to the Flask backend via a POST request to the /submit_complaint endpoint.

The app.py server receives the request, saves the form details in a timestamped .txt file in the complaints/ directory, and saves the uploaded screenshot in the uploads/ directory.

Thank you for visiting our project!

Readme file
