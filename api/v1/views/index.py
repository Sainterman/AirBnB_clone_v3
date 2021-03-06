#!/usr/bin/python3
""" API index template routing"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/status')
def status():
    """Return status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Retrieves number of each objects by type"""
    counts = dict()
    for name, clase in classes.items():
        counts.update({name: storage.count(clase)})
    return jsonify(counts)
