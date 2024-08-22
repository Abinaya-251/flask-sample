from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the Home Page..."

@app.route("/about")
def about():
    return "Hello from the About Page..."

if __name__ == "__main__":
    app.run(port=8000)