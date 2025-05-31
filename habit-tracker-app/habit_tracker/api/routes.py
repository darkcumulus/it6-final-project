from flask import Blueprint, jsonify, request
import sqlite3
from datetime import datetime

api_bp = Blueprint('api', __name__)

# GET all habits
@api_bp.route('/habits', methods=['GET'])
def get_habits():
    with sqlite3.connect('habit_tracker.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM habits")
        habits = cur.fetchall()
    return jsonify([dict(habit) for habit in habits])

# POST new habit
@api_bp.route('/habits', methods=['POST'])
def create_habit():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO habits (name, start_date) VALUES (?, ?)",
            (data['name'], datetime.now().strftime('%Y-%m-%d'))
        )
        conn.commit()
    return jsonify({"message": "Habit created"}), 201

# PUT update habit
@api_bp.route('/habits/<int:habit_id>', methods=['PUT'])
def update_habit(habit_id):
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        
        # First verify the habit exists
        cur.execute("SELECT id FROM habits WHERE id = ?", (habit_id,))
        if not cur.fetchone():
            return jsonify({"error": "Habit not found"}), 404
            
        # Update the habit
        cur.execute(
            "UPDATE habits SET name = ? WHERE id = ?",
            (data['name'], habit_id))
        
        # Get the updated habit
        cur.execute("SELECT * FROM habits WHERE id = ?", (habit_id,))
        updated_habit = cur.fetchone()
        conn.commit()
        
        if not updated_habit:
            return jsonify({"error": "Update failed"}), 500
            
    return jsonify(dict(updated_habit)), 200

# DELETE habit
@api_bp.route('/habits/<int:habit_id>', methods=['DELETE'])
def delete_habit(habit_id):
    with sqlite3.connect('habit_tracker.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        conn.commit()
    return '', 204
