from flask import Flask
from flask_migrate import Migrate
from models import db  # Import db from models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
