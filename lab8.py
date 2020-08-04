class Matrix(object):
    def __init__(self, matrix):
        '''(Matrix, list)-> NoneType
        creates a data attribute elements and instantiate it to the matrix.

        Preconditions: list e contains 2 sublists, all the sublists in e have the same length.

        Complete the instance variable definitions DO NOT CHANGE THE VARIABLE NAMES. Feel free to
        add new ones
        '''
        if len(matrix) == 0:
            return None
        self.elements = matrix
        self.cols = len(matrix[0]) # number of columns
        self.rows = len(matrix) # number of rows
   
    def __str__(self):
        '''(Matrix) -> str 
        returns a string representation of the elements of the matrix. When passed to print() this
        representation should result in the original matrix being displayed as follows: each row
        will be displayed on a separate line, with each element in a row separated from the next by
        one, and only one blank space. The string representation should not contain any additional
        blank spaces. Print nothing if the matrix is empty.

        >>> print(Matrix([[1,2], [3,4]]))
        1 2
        3 4
        >>> print(Matrix([[0,-1.5,2.0], [-1, 4.5, 0]]))
        0 -1.5 2.0
        -1 4.5 0 
        >>> print(Matrix([[]]))

        '''
        pass
        x=''
        for sublist in self.elements:
            n = 0
            while n < len(sublist):
                x += str(sublist[n])
                x += ' '
                n+=1
            if sublist != self.elements[len(self.elements)-1]:
                x += '\n'
        return x
    
    def __repr__(self):
        """Do not change this."""
        return self.__str__()

    def __eq__(self, other):
        ''' (Matrix) -> bool
        Returns if the self matrix is equal (elementwise) to the other matrix

        >>> Matrix([[1,1],[1,1]]) == Matrix([[1,1],[1,1]])
        True
        >>> Matrix([[1,1],[1,2]]) == Matrix([[1,1],[1,1]])
        False
        '''
        if self.elements == other.elements:
            return True
        else:
            return False
        pass

    def add(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Returns the result (as a new Matrix object) of adding the second input Matrix to the first.
        Return an empty matrix if the matrices has mismatching sizes.
        
        >>> Matrix([[1,1],[1,1]]).add(Matrix([[-1,3],[0,0]]))
        0 4
        1 1
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).add(Matrix([[2,-0.5,1],[0,0,0],[0,0,1]]))
        1 2.5 1
        0 0 0
        1.5 1 2
        '''
        pass
        if self.rows != other.rows or self.cols != other.cols:
            return []
        output = []
        range_of_matrix = range(0, self.rows)
        range_of_other = range(0, self.cols)
        for i in range_of_matrix:
            output_sublist = []
            for j in range_of_other:
                output_sublist.append(self.elements[i][j] + other.elements[i][j])
            output.append(output_sublist)  
        return Matrix(output)  
    
    def mul(self, k):
        '''(Matrix, Matrix) -> Matrix
        Returns the scalar product of the input matrix with scalar k as a new matrix onject.
        
        >>> Matrix([[1,1],[1,1]]).mul(1)
        1 1
        1 1
        >>> Matrix([[1,3],[-2,-1]]).mul(-1)
        -1 -3
        2 1
        '''
        pass
        output = []
        range_of_matrix = range(0, self.rows)
        range_of_other = range(0, self.cols)        
        for i in range_of_matrix:
            output_sublist = []
            for j in range_of_other:
                output_sublist.append(self.elements[i][j] * k)
            output.append(output_sublist)
        print(output)    
        return (Matrix(output))
    
    def sub(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Returns the result (as a new Matrix object) of subtract the second input Matrix to the
        first. Return an empty matrix if the matrices has mismatching sizes.

        >>> Matrix([[1,1],[1,1]]).sub(Matrix([[-1,3],[0,0]]))
        2 -2
        1 1
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).sub(Matrix([[2,-0.5,1],[0,0,0],[0,0,1]]))
        -3 3.5 -1
        0 0 0
        1.5 1 0
        '''
        pass
        if self.rows != other.rows or self.cols != other.cols:
            return []        
        output = []
        range_of_matrix = range(0, self.rows)
        range_of_other = range(0, self.cols)
        for i in range_of_matrix:
            output_sublist = []
            for j in range_of_other:
                output_sublist.append(self.elements[i][j] - other.elements[i][j])
            output.append(output_sublist)  
        return Matrix(output) 
        
    def trace(self):
        '''(Matrix) -> float
        Returns the trace of the input matrix as a floating point number. If the matrix is not
        square, return float('inf')

        >>> Matrix([[1,1],[2,2]]).trace() 
        3.0 
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).trace()
        0.0
        '''
        pass
        if self.rows != self.cols:
            return float('inf')
        output = 0
        range_of_matrix = range(0, self.rows)
        for i in range_of_matrix:
            output += self.elements[i][i]
        return float(output)
    
    def transpose(self):
        '''(Matrix) -> Matrix
        Returns the transpose of the input matrix as a new Matrix object.
        
        >>> Matrix([[1,2],[3,4]]).transpose()
        1 3
        2 4
        '''
        pass
        output = []
        index = 0
        columns = []
        while index < self.cols:
            sublist_of_columns = []    
            for sublist in self.elements:
                sublist_of_columns.append(sublist[index])
            columns.append(sublist_of_columns)   
            index += 1
        return Matrix(columns)
        
    def dot(self, other):
        '''(Matrix, Matrix) -> Matrix
        Returns a matrix product between self and other.

        If self and other has mismatching dimension, return an empty Matrix object. If not, return
        the result of self (dot) other

        >>> A = Matrix([[1,2],[3,4],[5,6]])
        >>> A.dot(A.transpose()) 
        5 11 17
        11 25 39
        17 39 61
        '''
        pass
        if self.cols != other.rows:
            return []
        columns = []
        output = []
        i = 0
        index = 0
        while index < other.cols:
            sublist_of_columns = []    
            for sublist in other.elements:
                sublist_of_columns.append(sublist[index])
            columns.append(sublist_of_columns)   
            index += 1
            
        while i < self.rows:
            k=0
            sublist_of_output = []
            while k < other.cols:
                x=0
                y = 0
                j = 0
                while j < other.rows:
                    x += self.elements[i][j] * other.elements[j][k]
                    j += 1
                y += x
                k += 1
                sublist_of_output.append(y)
            output.append(sublist_of_output)    
            i += 1    
                
        return Matrix(output)
                