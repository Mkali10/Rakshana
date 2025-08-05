from flask import Flask, request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import time
import os

app = Flask(__name__)
app.secret_key = os.environ.get('RAKSHANA_SECRET', 'change_this_secret_key')

# Watermark for uniqueness
WATERMARK = "Rakshana by Mkali10 - 2025-08-05"

# User data store - in prod, replace with DB or secure vault
users = {
    "admin": generate_password_hash("ChangeThisStrongPassword!")
}

login_attempts = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    ip = request.remote_addr
    now = time.time()
    login_attempts[ip] = [t for t in login_attempts.get(ip, []) if now - t < 300]

    if len(login_attempts[ip]) >= 5:
        return "Too many login attempts. Please wait and try again later.", 429

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            login_attempts[ip] = []
            return redirect(url_for('index'))
        else:
            login_attempts.setdefault(ip, []).append(now)
            return "Invalid credentials", 401

    return render_template('login.html')

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f"""
    <h1>Welcome to Rakshana Admin UI</h1>
    <p><small>{WATERMARK}</small></p>
    <p><a href='/logout'>Logout</a></p>
    """

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
