"""
matrix-api v0.1
@author Ben Hansen
@created on 04/11/2016
identity.py

JSON Schema for the identity endpoint. Specifies the structure
and types required in order for the request body to
be considered valid.
"""

identity = {
    "rows": int,
    "columns": int
}
