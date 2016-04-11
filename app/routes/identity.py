"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
identity.py

Route handler for the identity endpoint.
GET /v1/identity
"""

from flask import Flask, Blueprint, request, jsonify
from app.matrix import Matrix

identity = Blueprint('identity', __name__)

@identity.route('/v1/identity')
def getIdentity():
    return jsonify({'result': str(Matrix.identity())})
