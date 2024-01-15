from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace the following line with your RDS endpoint, database name, username, and password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://quint1234:quint1234@mydb.c5waemoyctjc.us-east-1.rds.amazonaws.com:3306/mydb'

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
