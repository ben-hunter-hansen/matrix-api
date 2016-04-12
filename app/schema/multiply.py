"""
matrix-api v0.1
@author Ben Hansen
@created on 04/11/2016
multiply.py

JSON Schema for the multiply endpoint. Specifies the structure
and types required in order for the request body to
be considered valid.
"""

multiply = {
    'operands': {
        'lvalue': list,
        'rvalue': list
    }
}
