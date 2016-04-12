"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
multiply.py

Route handler for the multiply endpoint.
POST /v1/multiply
"""

from flask import Flask, Blueprint, abort, request, jsonify
from app.matrix import Matrix
from app.decorators import validate
import app.schema

multiply = Blueprint('multiply', __name__)


@multiply.before_request
@validate(request, app.schema.multiply)
def buildMatricies(model):
    request.matrixA = Matrix.fromArray(model['lvalue'])
    request.matrixB = Matrix.fromArray(model['rvalue'])

@multiply.route('/v1/multiply', methods=["POST"])
def postMultiply():
    return jsonify((request.matrixA * request.matrixB).toKeyValuePair('result'))
