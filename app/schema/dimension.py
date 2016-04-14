"""
matrix-api v0.1
@author Ben Hansen
@created on 04/11/2016
dimension.py

JSON Schema for endpoints that accept matrix
dimensions. Specifies the structure
and types required in order for the request body to
be considered valid.
"""

dimension = {
    "rows": int,
    "columns": int
}
