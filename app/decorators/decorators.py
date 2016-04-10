"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
decorators.py
"""


import inspect

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
