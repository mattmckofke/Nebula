from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DATABASE = {
    'dbname': 'sqlflask',
    'user': 'postgres',
    'password': '1104',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    return psycopg2.connect(**DATABASE)

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    return "Welcome to the Flask API with psycopg2!"

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users WHERE id = %s LIMIT 1', (id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(user) if user else ('User not found', 404)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    name = new_user['name']
    email = new_user['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_user), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    updated_user = request.get_json()
    name = updated_user['name']
    email = updated_user['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(updated_user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)