from flask import Flask


app = Flask(__name__)


@app.register_blueprint(views, url_prefix="/views")


def home():
    return "this is the home page"


if __name__ == '__main__':
    app.run(debug=True, port=8000)