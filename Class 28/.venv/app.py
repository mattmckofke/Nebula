from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to the Flask Backend!"}
    
@app.route("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.route("/user/<username>")
def greet_user(username):
    return {"message": f"Hello, {username}"}

@app.route("/status")
def status():
    return {"status": "OK"}

@app.route("/square/<int:number>")
def square(number):
    result = number ** 2
    return {"square": result}

@app.route("/echo/<message>")
def echo(message):
    return {"echo": message}

@app.errorhandler(404)
def not_found(error):
    return {"error": "Not found"}, 404

@app.errorhandler(400)
def server_error(error):
    return {"error": "Invalid POST data"}

if __name__ == "__main__":
    app.run(debug=True)