#!/usr/bin/python3
"""web app index page"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the api"""
    return jsonify({"status": "OK"})
