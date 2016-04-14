"""
matrix-api v0.1
@author Ben Hansen
@created on 04/11/2016
binaryop.py

JSON Schema for endpoints that perform binary
matrix operations. Specifies the structure
and types required in order for the request body to
be considered valid.
"""

binaryop = {
    'operands': {
        'lvalue': list,
        'rvalue': list
    }
}
