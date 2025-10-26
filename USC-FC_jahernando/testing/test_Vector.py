import random
from Vector import Vector
import numpy as np
np.random.seed(1)
def inputs():

    a = [random.uniform(-1,1) for i in range(10)]
    b = [random.uniform(-1,1) for i in range(10)]
    
    return Vector(a), Vector(b)

def test_Vector_add():

    a, b = inputs()

    null = 0 * a

    assert a + b == b + a
    assert a + null == null + a
    assert a + (a + b) == (a + a) + b



def test_Vector_mul():

    a, b = inputs()

    assert 0 * a == a * 0
    assert 1 * a == a
    assert a * b == b * a  
    assert b[0] * (a + b) == b[0] * a + b[0] * b



def test_Vector_abs():

    a, b = inputs()
    assert abs(a) >= 0 


def test_Vector_neg():

    a, b = inputs()

    assert -a == (-1) * a



def test_Vector_sub():

    a, b = inputs()

    assert a - b == -(b - a)
    assert a - b == a + (-b)


def test_Vector_unit():

    a, b = inputs()

    assert np.isclose(abs(a.unit()), 1)
