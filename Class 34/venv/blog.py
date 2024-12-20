from flask import Flask, jsonify, request
import json
import os
import psycopg2
    
app = Flask(__name__)

DATABASE = {
       'dbname': 'blog_db',
       'user': 'postgres',
       'password': '1104',
       'host': 'localhost',
       'port': '5432'
   }

db = {
    "posts": {},
    "current_post_id": 1
}

if os.path.exists('db.json'):
    with open('db.json', 'r') as file:
        db = json.load(file)

def get_db_connection():
    return psycopg2.connect(**DATABASE)

def data_transfer_to_db():
    conn = get_db_connection()
    cur = conn.cursor()
    for key, post in db["posts"].items():
        cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s);", (post["title"], post["content"]))
    conn.commit()
    cur.close()
    conn.close()

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS posts;
        CREATE TABLE posts (
            post_id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            content VARCHAR(200)
        );
    """)
    cur.execute("INSERT INTO posts (title, content) VALUES ('seed title', 'seed content');")
    conn.commit()
    cur.close()
    conn.close()
    data_transfer_to_db()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Blog API!"})
# Success request
@app.route('/success')
def success(data):
    return jsonify({"status": "sucess", "data": data}), 200
# Error handler
@app.errorhandler(400)
def bad_request(msg):
    return jsonify({'error': msg}), 400
# Not Found Handler
@app.errorhandler(404)
def not_found(msg):
    return jsonify({'error': msg}), 404
    
# 1. GET /posts
@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT post_id, title, content FROM posts;")
    results = cur.fetchall()
    cur.close()
    conn.close()

    posts = []
    for row in results:
        posts.append({
            "post_id": row[0],
            "title": row[1],
            "content": row[2]
        })
        
    query_title = request.args.get('title', 'default')
    query_content = request.args.get('content', 'default')
    page = request.args.get('page', '1')  # Default to '1' if not provided
    page_size = request.args.get('size', '5')  # Default to '2' if not provided

    # Validate and convert page and size to integers
    try:
        query_page = int(page)
        query_page_size = int(page_size)
    except ValueError:
        return bad_request("'page' and 'size' must be valid integers.")
    
    if query_title != 'default':
        print(query_title)
        for value in posts:
            if query_title in value['title']:
                posts.append(value)

    if query_content != 'default':
        print(query_content)
        for value in posts:
            if query_content in value['content']:
                posts.append(value)
    
    # Pagination
    # 0, 1, 2, 3, 4
    # page 3 size 2-> idx = 4 ... 6
    # page 1 -> start_idx = (page - 1) * size & end_idx = start_idx + size
    start_idx = (query_page - 1) * query_page_size
    end_idx = start_idx + query_page_size

    if end_idx > len(posts):
        end_idx = len(posts)
    if start_idx >= len(posts):
        start_idx = len(posts) - query_page_size
        end_idx = len(posts)
    posts = posts[start_idx: end_idx]
    
    return {"status": "success", "data": posts}, 200

# 2. POST /posts
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.json
    if 'title' not in new_post or 'content' not in new_post:
        return bad_request('Bad request title or content not in json request')
    db['current_post_id'] += 1
    new_post['post_id'] = db['current_post_id']
    db['posts'][new_post['post_id']] = new_post
    #save_db()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s);", (new_post["title"], new_post["content"]))
    conn.commit()
    cur.close()
    conn.close()
    return success(new_post)
# 3. GET Post by ID
@app.route('/posts/<int:id>')
def get_post_by_id(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE post_id=%s", (id,))
    result = cur.fetchone()
    if not result:
        return not_found("No id found")
    cur.close()
    conn.close()
    post = {
        "id": result[0],
        "title": result[1],
        "content": result[2]
    }
    return success(post) 
    
# 4. PUT Update a Post
@app.route("/posts/<int:id>", methods=['PUT'])
def update_post(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE post_id=%s", (id,))
    result = cur.fetchone()
    if not result:
        return not_found("No id found")
    
    updated_post = request.json
    if 'title' in updated_post:
        cur.execute("UPDATE posts SET title=%s WHERE post_id=%s", (updated_post['title'], id))
    if 'content' in updated_post:
        cur.execute("UPDATE posts SET content=%s WHERE post_id=%s", (updated_post['content'], id))
    
    #save_db()
    conn.commit()
    cur.close()
    conn.close()
    return success(updated_post)
# 5. DELETE a Post
@app.route("/posts/<int:id>", methods=['DELETE'])
def delete_posts(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE post_id=%s", (id,))
    result = cur.fetchone()
    if not result:
        return not_found("No id found")
    
    cur.execute("DELETE FROM posts WHERE post_id=%s", (id,))
    #reset_post_id_sequence()
    #save_db()
    conn.commit()
    cur.close()
    conn.close()
    return success('Post Deleted')

#def reset_post_id_sequence():
#    conn = get_db_connection()
#    cur = conn.cursor()
    
#    cur.execute("""
#                SELECT SETVAL(
#                    pg_get_serial_sequence('posts', 'post_id'),
#                    COALESCE(MAX(post_id), 0)
#                ) FROM posts;
#                """)
#    conn.commit()
#    cur.close()
#    conn.close()

# Extra Challenge - Data Persistence
#def save_db():
#    with open('db.json', 'w') as file:
#       json.dump(db, file, indent=4)
        
initialize_db()

if __name__ == '__main__':
    app.run(debug=True)