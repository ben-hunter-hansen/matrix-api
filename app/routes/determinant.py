"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
determinant.py

Route handler for the determinant endpoint.
POST /v1/determinant
"""

from flask import Flask, Blueprint, abort, request, jsonify
from app.matrix import Matrix

determinant = Blueprint('determinant', __name__)

@determinant.route('/v1/determinant', methods=["POST"])
def postDeterminant():
    if not request.json or not 'matrix' in request.json:
        abort(400)

    matrix = Matrix.fromArray(eval(request.json['matrix']))
    result = {
        'determinant': str(matrix.determinant())
    }
    return jsonify({'result': result})
