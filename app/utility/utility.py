"""
matrix-api v0.1
@author Ben Hansen
@created on 04/11/2016
utility.py
"""
import copy

def traverse(obj, visit):
    """
    Traverses a nested dictionary,
    invoking a visit function on
    each key/value pair.

    """
    for k, v in obj.items():
        if not isinstance(v, dict):
            visit(k,v)
        else:
            visit(k, None)
            traverse(obj[k], visit)

def complement(A, B):
    """
    Given two sets A and B, return the
    complement of set A with respect to B.
    """
    return [x for x in A if x in B]
