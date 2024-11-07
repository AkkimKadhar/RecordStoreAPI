                             Full-Stack CRUD Application with React, Flask, and MongoDB

This project is a full-stack CRUD (Create, Read, Update, Delete) application built with React for the frontend, Flask for the backend API, and MongoDB for the database.It allows users to view, add, edit, and delete records in a database via a responsive data grid.


Installation
Prerequisites

* Node.js and npm: For running the React frontend.
Install Node.js and npm by downloading from Node.js Downloads.

* Python: Required to run the Flask backend.
Install Python by downloading from Python Downloads.

* MongoDB: Database to store application data.
Install MongoDB by downloading from MongoDB Community Server.

Backend Setup---->

Open a terminal and navigate to the backend directory.
Create a virtual environment

* pip install Flask pymongo Flask-CORS

Make sure MongoDB is running on your local machine or specify the MongoDB URI in the MongoClient connection in app.py.

Frontend Setup---->

Open a terminal and navigate to the frontend directory.
Install the required Node modules:

* npm install
* npm install @mui/material @mui/icons-material @mui/x-data-grid axios


Running the Application

Step 1: Start MongoDB
Ensure MongoDB is running on localhost:27017 or as specified in your app.py.

Step 2: Start the Backend Server In the backend directory.

* python app.py

step 3: Start the Flask server:

* npm start
* 
The application will be accessible at http://localhost:3000
