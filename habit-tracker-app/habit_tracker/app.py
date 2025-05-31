from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
try:
    from api.routes import api_bp
except ImportError:
    from .api.routes import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')  # Add this line

def init_db():
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_date TEXT NOT NULL,
            streak INTEGER DEFAULT 0
        )''')
        conn.commit()


@app.route('/')
def index():
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM habits")
        habits = cur.fetchall()
    return render_template('index.html', habits=habits)


@app.route('/add', methods=['POST'])
def add_habit():
    name = request.form['name']
    start_date = datetime.now().strftime('%Y-%m-%d')
    
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO habits (name, start_date) VALUES (?, ?)", (name, start_date))
        conn.commit()
    
    return redirect('/')

@app.route('/update_streak/<int:habit_id>', methods=['POST'])
def update_streak(habit_id):
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute("UPDATE habits SET streak = streak + 1 WHERE id = ?", (habit_id,))
        conn.commit()
    
    return redirect('/')


@app.route('/delete/<int:habit_id>', methods=['POST'])
def delete_habit(habit_id):
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        conn.commit()
    
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
