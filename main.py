from flask import Flask
from models import db, User  # Import the db instance from models.py and User model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite database for example
db.init_app(app)  # Initialize the db with the Flask app

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Check if the example user already exists
with app.app_context():
    user = User.query.filter_by(username='john_doe').first()

    # If the user doesn't exist, add the example user
    if not user:
        user1 = User(username='john_doe', email='john@example.com')
        db.session.add(user1)
        db.session.commit()

# Create a simple route
@app.route('/')
def index():
    users = User.query.all()  # Retrieve all users from the database
    user_list = [f"Username: {user.username}, Email: {user.email}" for user in users]

    return "\n".join(user_list)

if __name__ == '__main__':
    app.run()
