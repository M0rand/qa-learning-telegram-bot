from flask import Blueprint, jsonify, request

example_bp = Blueprint("example", __name__)

@example_bp.get("/")
def list_items():
    return jsonify({"items": [], "message": "Replace this with your own logic"})

@example_bp.post("/")
def create_item():
    data = request.get_json(silent=True) or {}
    return jsonify({"created": data}), 201
