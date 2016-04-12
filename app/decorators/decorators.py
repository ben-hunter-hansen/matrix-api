"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
decorators.py
"""

from flask import abort, jsonify
import inspect
import json
import app.utility

def require(**requirements):
    """
    Decorator for argument type requirements.  Ensures
    that if a supplied argument does not match the required type,
    an error is raised.

    e.x
    @require(a = int, b = int)
    def myMethod(self, a, b):
    """
    def decorator(f):
        argNames = inspect.getargspec(f)[0]
        strErr = f.__name__ +": Invalid argument types\nexpected " + str(requirements)

        # If a typical method is decorated
        def wrapNormalMethod(self, *args, **kwargs):
            argDict = dict(zip(argNames[1:], args))
            for key in argDict:
                if key in requirements and type(argDict[key]) != requirements[key]:
                    raise TypeError(strErr)
            return f(self, *args, **kwargs)

        # If a @classmethod is decorated
        def wrapClassMethod(cls, *args, **kwargs):
            argDict = dict(zip(argNames[1:], args))
            for key in argDict:
                if key in requirements and type(argDict[key]) != requirements[key]:
                    raise TypeError(strErr)
            return f(cls, *args, **kwargs)

        # If a @staticmethod or function is decorated
        def wrapStaticMethod(*args, **kwargs):
            argDict = dict(zip(argNames, args))
            for key in argDict:
                if key in requirements and type(argDict[key]) != requirements[key]:
                    raise TypeError(strErr)
            return f(*args, **kwargs)

        if 'self' in argNames:
            return wrapNormalMethod
        elif 'cls' in argNames:
            return wrapClassMethod
        else:
            return wrapStaticMethod

    return decorator


def validate(request, schema):
    """
    Validates the structure and type integrity of a
    json payload based off of a schema.  If the payload is
    valid json, but has missing or invalid properties, abort
    with a 422.

    """
    def decorator(f):
        def wrapper(*args, **kwargs):
            try:
                schemaProps, schemaTypes = app.utility.flatten(schema)
                requestProps, requestPairs = app.utility.flatten(request.json)
                complement = app.utility.complement(set(schemaProps), set(requestPairs.keys()))
            except ValueError: # Malformed JSON
                abort(400)

            model = {}

            for k in complement:
                parsedValue = json.loads(requestPairs[k])
                if isinstance(parsedValue, schemaTypes[k]):
                    model[k] = parsedValue

            if len(model.keys()) != len(complement): # Missing or invalid properties
                abort(422, {'required': str(schema), 'given': str(request.json)})

            return f(model,*args, **kwargs)
        return wrapper
    return decorator
