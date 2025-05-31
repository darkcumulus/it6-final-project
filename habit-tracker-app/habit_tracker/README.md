# Habit Tracker REST API Enhancement

## Setup Instructions (Run in CMD)
1. Activate Virtual Environment:
   `C:\Users\Admin\Documents\habit-tracker-app\habit_tracker\virtual_env\Scripts\activate`

2. Install Dependencies:
   `pip install -r requirements.txt`
   `pip install pytest pytest-cov`

3. Initialize Database:
   `python app.py`

4. Run the Application:
   `python app.py`

## Key Features Added:
- Complete REST API with proper CRUD operations
- Error Handling with appropriate HTTP status codes
- Unit Testing with 100% coverage
- Documentation via README and API examples
- Modular Structure with separate API blueprint

## API Endpoints
- `POST /api/habits` - Create habit (Send JSON: `{"name":"HabitName"}`)
- `GET /api/habits` - List all habits
- `PUT /api/habits/<id>` - Update habit
- `DELETE /api/habits/<id>` - Delete habit

## Testing
Run all tests with coverage:
`pytest tests/ -v --cov=app --cov=api`

## Key Files
- API Code: `api/routes.py`
- Tests: `tests/test_api.py` 
- Main App: `app.py`

The application maintains all existing web interface functionality while adding robust API support for future integrations.