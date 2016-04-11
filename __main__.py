"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
Application entry point.
"""


from flask import Flask, request, abort, json, after_this_request, jsonify
from app.matrix import Matrix

api = Flask(__name__)

@api.route('/v1/identity')
def getIdentity():
    return str(Matrix.identity())


@api.route('/v1/multiply', methods=["POST"])
def doMultiply():
    if not request.json or not 'operands' in request.json:
        abort(400)

    operands = request.json['operands']
    matrixA = Matrix.fromArray(eval(operands['rvalue']))
    matrixB = Matrix.fromArray(eval(operands['lvalue']))
    result = {
        'product': str(matrixA * matrixB)
    }
    return jsonify({'result': result})

if __name__ == "__main__":
    api.run(debug = True)
