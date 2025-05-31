import pytest
from app import app, db
from app.models import Author

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory DB for test
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

# --------------------
# POST /authors
# --------------------
def test_create_author_success(client):
    response = client.post('/authors', json={
        'name': 'George Lucas',
        'bio': 'Created Star Wars'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'George Lucas'
    assert data['bio'] == 'Created Star Wars'

def test_create_author_missing_name(client):
    response = client.post('/authors', json={'bio': 'No name'})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Name is required'

# --------------------
# GET /authors
# --------------------
def test_get_all_authors(client):
    with app.app_context():
        author = Author(name='John Doe', bio='Writer')
        db.session.add(author)
        db.session.commit()
    response = client.get('/authors')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1

# --------------------
# GET /authors/<id>
# --------------------
def test_get_author_success(client):
    with app.app_context():
        author = Author(name='Jane Austen', bio='Novelist')
        db.session.add(author)
        db.session.commit()
        author_id = author.id
    response = client.get(f'/authors/{author_id}')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Jane Austen'

def test_get_author_not_found(client):
    response = client.get('/authors/999')
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Author not found'

# --------------------
# PUT /authors/<id>
# --------------------
def test_update_author_success(client):
    with app.app_context():
        author = Author(name='Old Name', bio='Old Bio')
        db.session.add(author)
        db.session.commit()
        author_id = author.id
    response = client.put(f'/authors/{author_id}', json={
        'name': 'New Name',
        'bio': 'Updated Bio'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'New Name'
    assert data['bio'] == 'Updated Bio'

def test_update_author_not_found(client):
    response = client.put('/authors/999', json={'name': 'Ghost'})
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Author not found'

# --------------------
# DELETE /authors/<id>
# --------------------
def test_delete_author_success(client):
    with app.app_context():
        author = Author(name='To Delete', bio='Bye')
        db.session.add(author)
        db.session.commit()
        author_id = author.id
    response = client.delete(f'/authors/{author_id}')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Author deleted'

def test_delete_author_not_found(client):
    response = client.delete('/authors/999')
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Author not found'
