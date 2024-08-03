from flask import Flask #type:ignore
from flask import make_response #type:ignore

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "testing api aa"

if __name__ == '__main__':
    app.run(debug=True)