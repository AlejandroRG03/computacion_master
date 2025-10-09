from Vector3D import Vector3D

def test_abs(a):
    m = abs(a)
    assert m > 0                        #positivo

    return True



def test_add(a, b):

    null = a * 0
    
    assert a + b       == b + a         # simétrica
    assert a + null    == null + a      # elemento neutro es el cero
    assert a + (a + b) == (a + a) + b   # asociativa
    
    return True

def test_sub(a, b):

    null = a * 0

    assert a - b       == -b + a
    assert a - null    == -null + a 
    assert a - (a - b) == (a - a) + b

    return True
    
    
def test_mul(a, b):

    assert a * 0      == 0 * a         # 
    assert 1 * a      == a             # elemento neutro es el 1
    
    if isinstance(a, Vector3D) and isinstance(b, Vector3D):
        alpha = b[0]
        assert a * alpha  == alpha * a     # multiplicacion por un escalar
    
    else:
        assert b * a == a * b              # multiplicacion por un escalar

    return True

def test_unit(a):

    m = abs(a.unit())

    assert m <= 1. + 1e-6                      # el modulo de un vector unitario es 1
    assert m >= 1. - 1e-6
    return True

def test_neg(a):
    assert -a == (-1) * a
    assert a + (-a) == 0 * a

    return True

a = Vector3D(1,3,6)
b = Vector3D(2,4,6)

test_abs(a)
test_add(a, b)
test_sub(a, b)
test_mul(a, b)
test_unit(a)
test_neg(a)
print("All tests passed")