from flask import Blueprint


vies = Blueprint("views")

@vies.route("/")
def home():
    return "home page"