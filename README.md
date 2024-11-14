
LoomNote App

This is a simple web application built using Flask that allows users to create, display, and delete notes seamlessly. The project utilizes a SQLite database for persistent data storage and demonstrates fundamental skills in Flask, HTML templates, and SQL.

One of the more challenging aspects of building this application was figuring out a way to save user-entered data. In the earliest stages, the data would be lost each time the user refreshed the web browser. After my research, I discovered that using Flask would be a great solution since it is lightweight, easy to integrate with Python (the language I had already started developing the app with), and offers simple tools for managing data. By using Flask, I was able to persist user data using an SQLite database, ensuring that notes are stored even if the app is restarted or the page is refreshed.

Key Learnings
•	Flask Integration: I learned how to set up a Flask application to handle HTTP requests, manage routes, and serve both static and         dynamic content.
•	Database Setup: I explored how to use SQLite with Flask for storing and retrieving user data, which solved the problem of data           persistence.
•	HTML Structure: I learned the basics of creating an HTML page that acts as the front-end interface for displaying and interacting with   the app’s data.

Features
  • Add Notes: Users can submit text-based notes that are saved to a local SQLite database.
	•	Display Notes: The app retrieves and displays all saved notes on the main page.
	•	Delete Notes: Users can delete individual notes using a simple “delete” button.
	•	Database Persistence: Data is stored in an SQLite database, ensuring that notes persist between sessions.

 Tools Used
 	•	Flask: A lightweight Python web framework.
	•	SQLite: A simple, serverless database for storing notes.
	•	HTML/CSS: Basic templates for the user interface.
	•	Python: Core application logic.

 Setup and Installation
 - Prerequisites: Python 3.x
 1. Clone the repository: git clone https://github.com/YourUsername/flask-notes-app.git, then cd flask-notes-app
 2. Install dependencies: pip install -r requirements.txt
 3. Run the application: python app.py
 4. Access the app in your browser: Open http://127.0.0.1:5000 in your web browser.

 Usage
 1.	Enter a note in the text box and click Submit to add it.
 2.	The note will be displayed below the input form.
 3.	Click Delete next to any note to remove it from the list.

 Update 09.20.24, LoomNote currently can hold notes and can store them on SQLite database. There is also a feature to delete notes. With  time I want to add features that allow me to edit notes and to check them off as 'completed'
