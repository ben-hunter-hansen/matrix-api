"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
mathutil.py
"""

from app.decorators import require

@require(u = list, v = list)
def dot(u, v):
    """
    Given two vectors represented as
    one dimensional lists, return their
    dot product.

    @param u  (list)      First vector.
    @param v  (list)      Second vector.
    @return   (number)    The dot product of u and v

    """
    return sum(p * q for p, q in zip(u, v))
