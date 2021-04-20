from flask import Flask, request
from tanScore import getBestMatch

app = Flask(__name__)


@app.route('/')
def index():
    text = request.args.get("text")
    bestMatch = getBestMatch(text)
    return bestMatch


if __name__ == '__main__':
    app.run()
