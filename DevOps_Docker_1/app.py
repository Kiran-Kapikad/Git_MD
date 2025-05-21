from flask import Flask

app = Flask(__name__)  # Use __name__, not name

@app.route('/')
def hello():
    return "Hello, World from Kiran Kumar Kapikad!"

if __name__ == '__main__':  # Use __name__ == '__main__'
    app.run(host='0.0.0.0', port=5000)

