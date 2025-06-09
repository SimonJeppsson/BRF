from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'change-this-secret'

# Simple user database with roles
users = {
    'member': {'password': 'memberpass', 'role': 'member'},
    'board': {'password': 'boardpass', 'role': 'board'},
}

board_messages = []

@app.route('/')
def index():
    if 'username' in session:
        role = session.get('role')
        if role == 'board':
            return redirect(url_for('board_home'))
        return redirect(url_for('member_home'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = users.get(username)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
        if user['role'] == 'board':
            return redirect(url_for('board_home'))
        return redirect(url_for('member_home'))
    return render_template('login.html', error='Fel användarnamn eller lösenord')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/member')
def member_home():
    if session.get('role') != 'member':
        return redirect(url_for('index'))
    info = 'Information om din BRF'
    return render_template('member.html', info=info)

@app.route('/board')
def board_home():
    if session.get('role') != 'board':
        return redirect(url_for('index'))
    return render_template('board.html', messages=board_messages)

@app.route('/board/send', methods=['POST'])
def board_send():
    if session.get('role') != 'board':
        return redirect(url_for('index'))
    message = request.form.get('message')
    if message:
        board_messages.append(message)
    return redirect(url_for('board_home'))

if __name__ == '__main__':
    app.run(debug=True)
