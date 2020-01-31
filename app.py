import random
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/ready")
def ready():
    prob = random.random()
    if prob > 0.3:
        return "0k", 200
    else:
        return "No Ok", 500


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name: str = None):
    hostname = socket.gethostname()
    name = f"{name}, " if name else ''
    return f"{name} Greetings from {hostname}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
