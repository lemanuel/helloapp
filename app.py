import random
import socket

from flask import Flask

app = Flask(__name__)
__version__ = "v2.0"

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
    msg = f"[Host: {hostname}, ApiVersion: {__version__}]"
    return f"{name} Greetings from {msg}\n"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
