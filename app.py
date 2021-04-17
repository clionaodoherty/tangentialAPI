from flask import Flask, request
from tanScore import getBestMatch

app = Flask(__name__)


@app.route('/')
def index():
    text = request.args.get("text")
    if not text:
        return "No Text Given"
    bestMatch = getBestMatch(text)
    return bestMatch


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
