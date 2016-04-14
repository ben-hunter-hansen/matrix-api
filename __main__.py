"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
Application entry point.
"""


from flask import Flask, request, abort, json, after_this_request, jsonify
from app.matrix import Matrix
from app.routes import identity, determinant, multiply, add, sub

api = Flask(__name__)
api.register_blueprint(identity)
api.register_blueprint(determinant)
api.register_blueprint(multiply)
api.register_blueprint(add)
api.register_blueprint(sub)

@api.errorhandler(422)
def badRequest(error):
    return jsonify(error.description), 400

if __name__ == "__main__":
    api.run(debug = True)
