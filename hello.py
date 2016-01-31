from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    times = 3
    return "Hello World" * times


if __name__ == "__main__":
    app.debug = True
    app.run()
