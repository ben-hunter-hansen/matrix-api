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

            # Object containing the deserialized payload,
            # assuming it matches the schema.
            model = {}

            # As the request object is traversed, traverse the schema
            # in parallel. The schema defines the exact structure and
            # types required of the request object, so if they are not
            # in parallel then the request is invalid.
            visited = schema

            def visitor(k, v):

                nonlocal visited
                parsed = err = None

                if isinstance(v, dict): # Nested object
                    try:
                        visited = visited[k] # Next level
                    except KeyError: # Request is not structured correctly. Invalidate.
                        abort(422, {'required': str(schema), 'given': str(request.json)})
                    finally:
                        return # Bail out so the next level can be processed.

                parsed = json.loads(v) if isinstance(v, str) else v

                # visited[k] contains the required type specified by
                # the schema. Either add it to the model if the types are correct,
                # else invalidate.
                if isinstance(parsed, visited[k]):
                    model[k] = parsed
                else:
                    abort(422, {'required': str(schema), 'given': str(request.json)})

            # Traverse the request structure.
            app.utility.traverse(request.json, visitor)

            return f(model,*args, **kwargs)
        return wrapper
    return decorator
