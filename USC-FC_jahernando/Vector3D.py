import math
import numpy as np

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, v):

        if not isinstance(v, Vector3D):
            raise TypeError('the second operand must be a Vector3D')
        
        else:

            return Vector3D(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):

        if not isinstance(v, Vector3D):
            raise TypeError('the second operand must be a Vector3D')
        
        else:

            return Vector3D(self.x - v.x, self.y - v.y, self.z - v.z)
    
    def __mul__(self, v):

        if isinstance(v, int) or isinstance(v, float) or isinstance(v, complex):
            return Vector3D(self.x * v, self.y * v, self.z * v)
        
        elif isinstance(v, Vector3D):
            return self.x * v.x + self.y * v.y + self.z * v.z
        
        else:
            raise TypeError('the second operand must be a number or a Vector3D')
        
    def __rmul__(self, v):

        if isinstance(v, int) or isinstance(v, float) or isinstance(v, complex):
            return Vector3D(self.x * v, self.y * v, self.z * v)
        
        elif isinstance(v, Vector3D):
            return self.x * v.x + self.y * v.y + self.z * v.z
        
        else:
            raise TypeError('the second operand must be a number or a Vector3D')
        
    def cross(self, v):
    # cross product of two vectors

        if not isinstance(v, Vector3D):
            
            raise TypeError('the second operand must be a Vector3D')
        
        else:

            x = self.y * v.z - self.z * v.y
            y = self.z * v.x - self.x * v.z
            z = self.x * v.y - self.y * v.x

            return Vector3D(x, y, z)
    
    def __truediv__(self, a):

        if not (isinstance(a, int) or isinstance(a, float) or isinstance(a, complex)):
            raise TypeError('the second operand must be a number')
        
        if a == 0:
            raise ZeroDivisionError('division by zero')
        
        return Vector3D(self.x / a, self.y / a, self.z / a)
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, value):
        
        if not isinstance(value, Vector3D):
            return False
        return np.isclose(self.x, value.x) and np.isclose(self.y, value.y) and np.isclose(self.z, value.z)
    
    def unit(self):
        """ return the unit vector
        """
        mod = abs(self)
        if mod == 0:
            raise ZeroDivisionError('division by zero')
        return self / mod
    
    def __neg__(self):
        """ return the negative vector
        """
        return Vector3D(self.x, self.y, self.z) * -1
    
    def __getitem__(self, index):
        
        return [self.x, self.y, self.z][index]

    def __setitem__(self, index, value):

        ls = [self.x, self.y, self.z]
        ls[index] = value

        return Vector3D(ls[0], ls[1], ls[2])