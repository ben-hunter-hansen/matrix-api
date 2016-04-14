"""
matrix-api v0.1
@author Ben Hansen
@created on 04/14/2016
multiply.py

Route handler for the addition endpoint.
POST /v1/add
"""

from flask import Flask, Blueprint, abort, request, jsonify
from app.matrix import Matrix
from app.decorators import validate
import app.schema

add = Blueprint('add', __name__)


@add.before_request
@validate(request, app.schema.binaryop)
def buildMatricies(model):
    request.matrixA = Matrix.fromArray(model['lvalue'])
    request.matrixB = Matrix.fromArray(model['rvalue'])

@add.route('/v1/add', methods=["POST"])
def postAddition():
    return jsonify((request.matrixA + request.matrixB).toKeyValuePair('result'))
