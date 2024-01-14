from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace the following line with your RDS endpoint, database name, username, and password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@rds-endpoint:3306/mydb_instance'

db = SQLAlchemy(app)

class DummyText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))

@app.route('/')
def index():
    dummy_text = DummyText.query.first()
    return f'<h1>{dummy_text.text}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
