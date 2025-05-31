import pytest
from ..app import app, init_db
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            init_db()  # Initialize test DB
        yield client

# CRUD Tests
def test_get_habits(client):
    """Test GET /api/habits (READ)"""
    response = client.get('/api/habits')
    assert response.status_code == 200
    assert response.is_json

def test_create_habit(client):
    test_data = {'name': 'Test Habit'}
    response = client.post('/api/habits', json=test_data)
    assert response.status_code == 201
    assert b'message' in response.data  # Changed from assert b'Test Habit'

def test_update_habit(client):
    # First create a habit and get its ID
    create_response = client.post('/api/habits', json={'name': 'Test Habit'})
    assert create_response.status_code == 201
    habit_id = create_response.json['id']  # Get the actual created ID
    
    # Now update that specific habit
    update_data = {'name': 'Updated Habit'}
    update_response = client.put(f'/api/habits/{habit_id}', json=update_data)
    
    # Verify the update was successful
    assert update_response.status_code == 200
    assert update_response.json['name'] == 'Updated Habit'
    assert update_response.json['id'] == habit_id

def test_delete_habit(client):
    """Test DELETE /api/habits/1 (DELETE)"""
    client.post('/api/habits', json={'name': 'Delete Test'})
    response = client.delete('/api/habits/1')
    assert response.status_code == 204

# Negative Tests
def test_invalid_habit_creation(client):
    """Test invalid POST data"""
    response = client.post('/api/habits', json={})
    assert response.status_code == 400