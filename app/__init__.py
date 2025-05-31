from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # No need to set static_folder now
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
from app.author_routes import author_bp
app.register_blueprint(author_bp)

# Swagger UI
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={'app_name': "Author API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)



