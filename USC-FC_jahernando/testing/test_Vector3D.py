import random
from Vector3D import Vector3D
import numpy as np
np.random.seed(1)
def inputs():

    a = (random.uniform(-1,1) for i in range(3))
    b = (random.uniform(-1,1) for i in range(3))
    
    return Vector3D(*a), Vector3D(*b)

def test_Vector3D_add():

    a, b = inputs()

    null = 0 * a

    assert a + b == b + a
    assert a + null == null + a
    assert a + (a + b) == (a + a) + b



def test_Vector3D_mul():

    a, b = inputs()

    assert 0 * a == a * 0
    assert 1 * a == a
    assert a * b == b * a  
    assert b[0] * (a + b) == b[0] * a + b[0] * b



def test_Vector3D_abs():

    a, b = inputs()
    assert abs(a) >= 0 

def test_Vector3D_cross():

    a, b = inputs()

    assert a.cross(b) == - b.cross(a)
    assert a.cross(a) == a*0
    assert np.isclose(a * (a.cross(b)), 0)



def test_Vector3D_neg():

    a, b = inputs()

    assert -a == (-1) * a



def test_Vector3D_sub():

    a, b = inputs()

    assert a - b == -(b - a)
    assert a - b == a + (-b)


def test_Vector3D_unit():

    a, b = inputs()

    assert np.isclose(abs(a.unit()), 1)
