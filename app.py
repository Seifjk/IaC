from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@postgres:5432/mydatabase'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))

@app.route('/')
def hello():
    message = Message.query.first()
    return f"Hello, {message.content}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
