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

multiply = Blueprint('multiply', __name__)


@multiply.route('/v1/multiply', methods=["POST"])
def postMultiply():
    if not request.json or not 'operands' in request.json:
        abort(400)

    operands = request.json['operands']
    matrixA = Matrix.fromArray(eval(operands['lvalue']))
    matrixB = Matrix.fromArray(eval(operands['rvalue']))
    result = {
        'product': str(matrixA * matrixB)
    }
    return jsonify({'result': result})
