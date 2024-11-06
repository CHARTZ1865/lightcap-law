from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database URI (replace with your PythonAnywhere username)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://CHARTZ1865:AnaSofia1865!@CHARTZ1865.mysql.pythonanywhere-services.com/CHARTZ1865$feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    def __init__(self, content):
        self.content = content

# Route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get feedback from the form
        feedback_content = request.form['feedback']
        # Create new feedback entry
        new_feedback = Feedback(content=feedback_content)
        # Add to the database
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    # Create the database tables if they don't exist
    if not os.path.exists('feedback.db'):
        db.create_all()
    app.run()