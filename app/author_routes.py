from flask import Blueprint, request, jsonify
from app import db
from app.models import Author

author_bp = Blueprint('authors', __name__, url_prefix='/authors')

# Create
@author_bp.route('', methods=['POST'])
def create_author():
    data = request.get_json()
    name = data.get('name')
    bio = data.get('bio')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    new_author = Author(name=name, bio=bio)
    db.session.add(new_author)
    db.session.commit()
    return jsonify(new_author.to_dict()), 201

# Read All
@author_bp.route('', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([a.to_dict() for a in authors]), 200

# Read One by ID
@author_bp.route('/<int:id>', methods=['GET'])
def get_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({"error": "Author not found"}), 404
    return jsonify(author.to_dict()), 200

# Update
@author_bp.route('/<int:id>', methods=['PUT'])
def update_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({"error": "Author not found"}), 404

    data = request.get_json()
    author.name = data.get('name', author.name)
    author.bio = data.get('bio', author.bio)
    db.session.commit()
    return jsonify(author.to_dict()), 200

# Delete
@author_bp.route('/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({"error": "Author not found"}), 404

    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author deleted"}), 200
