# habit-tracker-app
The Habit Tracker App is a simple and intuitive web application built using Python and Flask to help users track and maintain their habits.
Habit Tracker App

Overview
The Habit Tracker App is a simple and intuitive web application built using Python and Flask to help users track and maintain their habits. Users can create, manage, and track daily habits, view their current streaks, and mark their habits as completed. The app stores all data in a SQLite database, ensuring users can always track their progress.

This project is perfect for those looking to develop personal productivity tools or demonstrate backend and frontend web development skills. It is fully customizable and can be extended to include more advanced features like user authentication, notifications, and progress visualization.

Features
Add new habits to track.
View all active habits with start dates and current streaks.
Mark habits as "done" for the day, which updates the streak.
Delete habits that are no longer needed.
Simple and responsive user interface with Flask rendering templates.
Backend powered by Python and Flask.
Data stored in an SQLite database for persistence.


Technologies Used
Python (Backend)
Flask (Web Framework)
SQLite (Database)
HTML/CSS (Frontend)

Setup and Installation
1. Clone the Repository
git clone https://github.com/soumitri27/habit-tracker-app.git
cd habit-tracker-app


3. Install Dependencies
You need Python 3.x installed on your system. Then, install Flask via pip:



pip install flask
3. Run the Application



python app.py
4. Open in Browser
Visit http://127.0.0.1:5000/ in your browser to access the app.

Usage
Add Habit:

Enter the habit you want to track in the input box and click "Add Habit".
Your new habit will appear with the start date and streak set to 0.
Mark Habit as Done:

Click the "Mark as Done" button next to a habit once you complete it for the day.
This will update the streak counter.
Delete Habit:

Click the "Delete" button to remove a habit from the list if you no longer want to track it.
