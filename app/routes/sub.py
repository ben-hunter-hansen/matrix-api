"""
matrix-api v0.1
@author Ben Hansen
@created on 04/14/2016
multiply.py

Route handler for the subtraction endpoint.
POST /v1/add
"""

from flask import Flask, Blueprint, abort, request, jsonify
from app.matrix import Matrix
from app.decorators import validate
import app.schema

sub = Blueprint('sub', __name__)

@sub.before_request
@validate(request, app.schema.binaryop)
def buildMatricies(model):
    request.matrixA = Matrix.fromArray(model['lvalue'])
    request.matrixB = Matrix.fromArray(model['rvalue'])

@sub.route('/v1/sub', methods=["POST"])
def postSubtraction():
    return jsonify((request.matrixA - request.matrixB).toKeyValuePair('result'))
