from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "success",
            "message": "Welcome to the Flask Backend!"}

@app.route("/status")
def status():
    return {"status": "API is running"}

@app.route("/reverse/<string:text>")
def reverse(text):
    return {"status": "success",
            "reverse": text[::-1]}

@app.route("/sum/<numbers>")
def get_sum(numbers):
    try:
        numbers = list(map(int, numbers.split("_")))
        return {"status": "success",
                "sum": sum(numbers)}
    except ValueError:
        return {"status": "Bad",
                "message": "Invalid input, ensure all numbers are integers seperated by _"}, 400

@app.route("/filter/<string:keyword>")
def filter(keyword):
    return {"status": "success",
            keyword: len(keyword)}

@app.route("/factorial/<int:num>")
def factorial(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    
    return {"status": "success",
            "factorial": f}

if __name__ == "__main__":
    app.run(debug=True)