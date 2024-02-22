from flask import Flask, render_template, request
from models import db, Message
from datetime import datetime

app = Flask(__name__)

# Налаштування бази даних PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    # Отримуємо дані з форми
    username = request.form['username']
    message = request.form['message']

    # Отримуємо поточний час
    now = datetime.now()

    # Зберігаємо повідомлення в базі даних
    new_message = Message(username=username, message=message, timestamp=now)
    db.session.add(new_message)
    db.session.commit()

    return 'Message received!'

if __name__ == '__main__':
    app.run(debug=True)
