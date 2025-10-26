import math 
import numpy as np

class Vector:

    def __init__(self, components):

        self.components = components
        return
    
    def __len__(self):
        return len(self.components)
    
    def __abs__(self):

        sum_sq = sum(c**2 for c in self.components)
        return math.sqrt(sum_sq)
    
    def __add__(self, v):

        if not isinstance(v, Vector):
            raise TypeError('the second operand must be a Vector')
        
        if len(v) != len(self):
            raise ValueError('the two vectors must have the same dimension')
        
        components = [self.components[i] + v.components[i] for i in range(len(self))]
        return Vector(components)
    
    def __sub__(self, v):

        if not isinstance(v, Vector):
            raise TypeError('the second operand must be a vector')
        
        if len(v) != len(self):
            raise ValueError('the two vectors must have the same dimension')
        
        components = [self.components[i] - v.components[i] for i in range(len(self))]
        return Vector(components)
    
    def __mul__(self, v):
        
        if isinstance(v, int) or isinstance(v, float) or isinstance(v, complex):
            components = [c * v for c in self.components]
            return Vector(components)
        
        elif isinstance(v, Vector):

            if len(v) != len(self):
                raise ValueError('the two vectors must have the same dimension')
            
            else:
                return sum(self.components[i] * v.components[i] for i in range(len(self)))
        
        else:
            raise TypeError('the second operand must be a number or a Vector')
    
    def __rmul__(self,v):
        return self * v
    
    def __truediv__(self, a):

        if not (isinstance(a, int) or isinstance(a, float) or isinstance(a, complex)):
            raise TypeError('the second operand must be a number')
        
        if a == 0:
            raise ZeroDivisionError('division by zero')
        
        components = [c / a for c in self.components]
        return Vector(components)
    
    def unit(self):

        mod = abs(self)

        if mod == 0:

            raise ZeroDivisionError('division by zero')
        
        return self / mod

    def __eq__(self, value):
        
        if not isinstance(value, Vector):
            return False
        
        if len(value) != len(self):
            return False

        for i in range(len(self)):

            if not np.isclose(self.components[i], value.components[i]):

                return False
            
        return True

    
    def __neg__(self):

        components = [-c for c in self.components]
        return Vector(components)

    def __str__(self):
        
        vec = '('

        for i in range(len(self.components)-1):
            vec += str(self.components[i]) + ', '

        vec += str(self.components[-1]) + ')'

        return vec
    
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        self.components[index] = value
