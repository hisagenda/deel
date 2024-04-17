from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('ips.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reversed_ips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route to handle requests
@app.route('/')
def index():
    # Get the user's IP address
    user_ip = request.remote_addr
    
    # Reverse the IP address
    reversed_ip = '.'.join(user_ip.split('.')[::-1])
    
    # Store the reversed IP in the database
    conn = sqlite3.connect('ips.db')
    c = conn.cursor()
    c.execute('INSERT INTO reversed_ips (ip) VALUES (?)', (reversed_ip,))
    conn.commit()
    conn.close()
    
    # Return the reversed IP
    return f'Your reversed IP address is: {reversed_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)