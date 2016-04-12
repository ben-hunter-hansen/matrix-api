"""
matrix-api v0.1
@author Ben Hansen
@created on 04/11/2016
utility.py
"""
import copy

def flatten(nested, keys = [], values = {}):
    """
    Traverses a nested dictionary structure and
    returns a list of the keys it contains, and
    a dictionary of all key/value pairs where the value
    is not itself another dictionary.

    """
    for k, v in nested.items():
        if k not in keys:
            keys.append(k)
        if isinstance(v, dict):
            keys, values = flatten(v, keys, copy.deepcopy(values))
        else:
            values[k] = v

    return keys, values

def complement(A, B):
    """
    Given two sets A and B, return the
    complement of set A with respect to B.
    """
    return [x for x in A if x in B]
