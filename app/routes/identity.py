"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
identity.py

Route handler for the identity endpoint.
POST /v1/identity
"""

from flask import Flask, Blueprint, abort, request, jsonify
from app.decorators import validate
from app.matrix import Matrix
import app.schema

identity = Blueprint('identity', __name__)


@identity.before_request
@validate(request, app.schema.dimension)
def buildIdentityMatrix(model):
    request.identity = Matrix(model["rows"], model["columns"]).identity()

@identity.route('/v1/identity', methods = ["POST"])
def getIdentity():
    return jsonify(request.identity.toKeyValuePair('identity'))
