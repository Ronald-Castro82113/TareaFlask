from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return jsonify({"status": "sucess", "menssage": "Mi primer proyecto en Flask"})