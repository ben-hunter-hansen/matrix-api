"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
determinant.py

Route handler for the determinant endpoint.
POST /v1/determinant
"""


from flask import Flask, Blueprint, abort, request, jsonify
from app.decorators import validate
from app.matrix import Matrix
import app.schema

determinant = Blueprint('determinant', __name__)

@determinant.before_request
@validate(request, app.schema.unaryop)
def computeDeterminant(model):
    request.det = Matrix.fromArray(model['matrix']).determinant()


@determinant.route('/v1/determinant', methods=["POST"])
def postDeterminant():
    return jsonify({ 'determinant': request.det })
