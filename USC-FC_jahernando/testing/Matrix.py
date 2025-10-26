import math
import numpy as np


class Matrix:

    def __init__(self, rows):

        self.rows = rows
        return
    
    def __str__(self):
        
        string = ''
        for row in self.rows:
            for elem in row:

                string += str(elem) + ' '
            
            string += '\n'

        return string
    
    def __repr__(self):
        return str(self)

    def __len__(self):
        """return the number of rows of the matrix"""
        return len(self.rows)
    
    def shape(self):
        
        return len(self.rows), len((self.rows[0]))
    
    def T(self):
        """traspose of the matrix"""
        m,n = self.shape()

        rows_T = [[self.rows[j][i] for j in range(m)] for i in range(n)]

        return Matrix(rows_T)
    

    def __add__(self, M):

        if not isinstance(M, Matrix):
            raise TypeError('the second operand must be a Matrix')
        
        if self.shape() != M.shape():
            raise ValueError('the two matrices must have the same shape')
        
        m, n  = self.shape()

        rows = [[self.rows[i][j] + M.rows[i][j] for j in range(n)] for i in range(m)]
        
        return Matrix(rows)
    
    def __sub__(self, M):
        
        if not isinstance(M, Matrix):
            raise TypeError('the second operand must be a Matrix')
        
        if self.shape() != M.shape():
            raise ValueError('the two matrices must have the same shape')
        
        m, n  = self.shape()

        rows = [[self.rows[i][j] - M.rows[i][j] for j in range(n)] for i in range(m)]
        
        return Matrix(rows)
    
    ''' more complex __getitem__

    def __getitem__(self, index):
        """Return an element M[i,j] or a submatrix M[i1:i2, j1:j2]"""
        if not isinstance(index, tuple):
            """if we don't have a tuple, return all columns"""
            index = (index, slice(0, len(self.rows[0]), 1))
            

        i1, i2 = index

        def range_slice(i, size):
        
            if isinstance(i, slice):
                start = i.start if i.start is not None else 0
                stop  = i.stop if i.stop  is not None else size
                step  = i.step  if i.step  is not None else 1
                return [x for x in range(start, stop, step) if x in range(size)]
            else:
                return [i]

        range_i1 = range_slice(i1, len(self.rows))
        range_i2 = range_slice(i2, len(self.rows[0]))
        
        if len(range_i1) == 1 and len(range_i2) == 1:
            return self.rows[range_i1[0]][range_i2[0]]
    
        return Matrix([[self.rows[i][j] for j in range(len(self.rows[0])) if j in range_i2] for i in range(len(self.rows)) if i in range_i1])
    
    '''
    
    def __getitem__(self, index):
        """"Return an element M[i,j]"""

        if not isinstance(index, tuple):
            
            return self.rows[index]

        i, j = index
        return self.rows[i][j]

    def __setitem__(self, index, value):
        """Set an element M[i,j]"""

        if not isinstance(index, tuple):
            
            self.rows[index] = value
        
        else:
            i, j = index
            self.rows[i][j] = value

    def __mul__(self, M):

        if isinstance(M, int) or isinstance(M, float) or isinstance(M, complex):
            """scalar multiplication"""
            m, n  = self.shape()

            rows = [[self.rows[i][j] * M for j in range(n)] for i in range(m)]
            
            return Matrix(rows)
        
        elif isinstance(M, Matrix):
            """matrix multiplication"""
            m1, n1 = self.shape()
            m2, n2 = M.shape()

            if n1 != m2:
                raise ValueError('ncols of the first matrix must be equal to nrows of the second matrix')
            

            rows = [[sum(self.rows[i][k] * M.rows[k][j] for k in range(n1)) for j in range(n2)] for i in range(m1)]
            
            return Matrix(rows)

        else:
            raise TypeError('the second operand must be a number or a Matrix')
        
    def __rmul__(self, M):

        if isinstance(M, int) or isinstance(M, float) or isinstance(M, complex):
            return self * M
        
        elif isinstance(M, Matrix):
            return M * self
        else:
            raise TypeError('the second operand must be a number or a Matrix')
        
    def __truediv__(self, k):

        if not (isinstance(k, int) or isinstance(k, float) or isinstance(k, complex)):
            raise TypeError('the second operand must be a number')
        
        if k == 0:
            raise ZeroDivisionError('division by zero')
        
        else:

            return self * (1 / k)
    
    def __neg__(self):
        return self * -1
    
    def __eq__(self, M):

        m1, n1 = self.shape()
        m2, n2 = M.shape()

        if m1 != m2 or n1!=n2:
            return False
        
        for i in range(m1):
            for j in range(n1):

                if not np.isclose(self[i,j], M[i,j]):
                    return False
        
        return True
