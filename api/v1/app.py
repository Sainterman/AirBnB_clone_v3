#!/usr/bin/python3
""" REST API module with flask"""
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, make_response, jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """tear down flask application"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """not found"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    ApiPort = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=ApiPort, threaded=True)
