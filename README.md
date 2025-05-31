# Flask CRUD Example with Authors API

## Project Overview

This is a simple Flask web application demonstrating CRUD (Create, Read, Update, Delete) REST API functionality for managing entries and authors.  
It uses Flask, SQLAlchemy for ORM, and Flask-Migrate for database migrations.  
Swagger UI is integrated for interactive API documentation.

---

## Features

- CRUD operations for `Entry` model (title, description, status)  
- CRUD REST API for `Author` model (name, bio) implemented using Flask Blueprint  
- RESTful API endpoints with JSON request/response format and proper HTTP status codes  
- Swagger UI documentation available at `/docs`  
- Unit tests covering all API functionality using `pytest`

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/gurkanakdeniz/example-flask-crud.git
   cd example-flask-crud


2. Create a virtual environment and activate it:

	python -m venv iptvenv
	iptvenv\Scripts\activate

3. Install dependencies:

	pip install -r requirements.txt

4. Initialize the database:
   (You only need to run flask db init once if not done before)

	flask db init
	flask db migrate -m "Add Author model"
	flask db upgrade


5. Run the application:

	python crudapp.py

---

## Usage
1. Access the main page for managing entries:
http://localhost:5000

2. Access authors UI:
http://localhost:5000/authors_ui

3. REST API endpoints are documented and available via Swagger UI:
http://localhost:5000/docs

REST API Endpoints for Author
Method	Endpoint	Description
GET	/authors	List all authors
POST	/authors	Create new author
GET	/authors/<id>	Get author by ID
PUT	/authors/<id>	Update author by ID
DELETE	/authors/<id>	Delete author by ID

--- 

## API Documentation
1. Interactive API documentation is available via Swagger UI at:
http://localhost:5000/docs

(If flask-swagger-ui is not installed, install it using:)

	pip install flask-swagger-ui

---

## Testing
1. If pytest is not installed, install it:

	pip install pytest

2. Run tests with:

	pytest test_author_api.py

---

## Changes I Made

1. I added a new feature: the Author Management API.

2. I created a new `Author` model with fields `name` and `bio` in `models.py`, and added a `to_dict()` method to help serialize author data to JSON.

3. I implemented a RESTful API for the Author model using a Flask Blueprint in `author_routes.py`.

4. I developed full CRUD functionality with JSON request and response formats, making sure to use proper HTTP status codes.

5. I registered the Author blueprint in the app’s `__init__.py` file.

6. I integrated Swagger UI for API documentation by adding an OpenAPI-compliant `swagger.json` under the static folder and configured it to serve at the `/docs` endpoint.

7. I wrote unit tests in `test_author_api.py` to cover all CRUD operations, including both positive and negative test cases, and achieved full test coverage using `pytest`.

8. I added a simple HTML UI for authors accessible at `/authors_ui` as an optional enhancement.

9. Finally, I updated `requirements.txt` to include `flask-swagger-ui` and `pytest`.

---

## Passed by: Glenn Paul Bryan Dela Cruz
## IPT Final Hands on activity
