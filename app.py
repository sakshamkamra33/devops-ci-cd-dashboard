from flask import Flask, request, jsonify, render_template
import sqlite3
import jwt
import datetime
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

# ---------------- DB SETUP ----------------
def init_db():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY,
        message TEXT,
        timestamp TEXT
    )''')

    # Default user
    c.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', '123')")

    conn.commit()
    conn.close()

init_db()

# ---------------- AUTH DECORATOR ----------------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'message': 'Token missing'}), 401

        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)

    return decorated

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/status')
@token_required
def status():
    return jsonify(status="Running", version="2.0.0")


@app.route('/logs')
@token_required
def get_logs():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("SELECT message, timestamp FROM logs ORDER BY id DESC LIMIT 10")
    logs = c.fetchall()

    return jsonify(logs=logs)


@app.route('/add-log', methods=['POST'])
def add_log():
    data = request.json
    msg = data.get('message')

    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs (message, timestamp) VALUES (?, ?)",
              (msg, str(datetime.datetime.now())))
    conn.commit()

    return jsonify({'message': 'Log added'})


@app.route('/about')
def about():
    return jsonify(message="Advanced DevOps project with auth, DB, logs")

# ---------------- RUN ----------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)