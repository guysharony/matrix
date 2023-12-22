from classes.vector import Vector


class Matrix:
    """
    A class to represent a matrix.
    """

    def __init__(self, data: list[list[float]]):
        """
        Initializes a matrix with the provided data.

        Complexity:
            Time: O(m)
            Space: O(mn)

        Args:
            data (list[list[float]]): A list containing elements representing the matrix.
        """

        try:
            if data.__class__ != list: # Operations have complexity of O(1)
                raise ValueError("Matrix values must be of type list of list.")

            if not all(len(row) == len(data[0]) for row in data): # Iterates through each row so time complexity of O(m)
                raise ValueError("Matrix rows must be the same size.")

            self.data = data
        except Exception as err:
            print(f'error: {err}')

    def __str__(self) -> str:
        """
        Returns the string representation of the matrix.

        Complexity:
            Time: O(mn)
            Space: O(mn)

        Returns:
            str: A string representation of the matrix.
        """

        return str(self.data)

    def __getitem__(self, index: int) -> list[float]:
        """
        Retrieve an element from the data list by index.

        Complexity:
            Time: O(1)
            Space: O(n)

        Args:
            index (int): The index of the element to retrieve.

        Returns:
            float: The element from the data list at the specified index.
        """
        return self.data[index]

    def get_shape(self) -> tuple[int, int]:
        """
        Retrieve the shape of the matrix.

        Complexity:
            Time: O(1)
            Space: O(1)

        Returns:
            tuple[int, int]: A tuple representing the shape (number of rows and columns) of the matrix.
        """
        return len(self.data), len(self.data[0])

    def add(self, v: 'Matrix') -> 'Matrix':
        """
        Adds another matrix to this matrix.

        Complexity:
            Time: O(mn)
            Space: O(mn)

        Args:
            v (Matrix): Another matrix to be added.

        Returns:
            Matrix: This matrix after addition.
        """
        v_rows, v_columns = v.get_shape() # Space and time complexity of O(1).
        rows, columns = self.get_shape() # Space and time complexity of O(1).

        if rows != v_rows or columns != v_columns: # Raise error if matrices have different shape.
            raise ValueError("Matrices must have the same dimensions for addition.")

        self.data = [[x + y for x, y in zip(a, b)] for a, b in zip(self, v)] # Loops rows m times and each column n times so complexity of O(mn).
        return self

    def sub(self, v: 'Matrix') -> 'Matrix':
        """
        Subtract another matrix from this matrix.

        Complexity:
            Time: O(mn)
            Space: O(mn)

        Args:
            v (Matrix): Another matrix to be subtracted.

        Returns:
            Matrix: This matrix after subtraction.
        """
        v_rows, v_columns = v.get_shape() # Space and time complexity of O(1).
        rows, columns = self.get_shape() # Space and time complexity of O(1).

        if rows != v_rows or columns != v_columns: # Raise error if matrices have different shape.
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        self.data = [[x - y for x, y in zip(a, b)] for a, b in zip(self, v)] # Loops rows m times and each column n times so complexity of O(mn).
        return self

    def scl(self, k: float) -> 'Matrix':
        """
        Scales this matrix by a factor.

        Complexity:
            Time: O(mn)
            Space: O(mn)

        Args:
            k (float): The scaler.

        Returns:
            Matrix: This matrix after scaling.
        """

        self.data = [[x * k for x in row] for row in self] # Create a matrice of m rows and n columns so complexity of O(mn).
        return self

    def mul_vec(self, vec: 'Vector') -> 'Vector':
        """
        Multiplies the matrix by a vector.

        Complexity:
            Time: O(nm)
            Space: O(n)

        Args:
            vec (Vector): The vector to be multiplied with the matrix.

        Returns:
            Vector: A new Vector resulting from the matrix-vector multiplication.
        """

        v_length = vec.get_size() # Space and time complexity of O(1).
        rows, columns = self.get_shape() # Space and time complexity of O(1).

        if columns != v_length: # Raise error if number of columns in the matrix is different than vector's length.
            raise ValueError("Matrix columns must match vector length for multiplication.")

        result = [0] * v_length # Create a list of size n.

        for n in range(columns): # Iterates through columns n times.
            for m in range(rows): # Iterates through rows m times.
                result[m] += self[m][n] * vec[n]

        return Vector(result) # Creating a vector of size n.

    def mul_mat(self, mat: 'Matrix') -> 'Matrix':
        """
        Multiplies two matrices.

        Complexity:
            Time: O(nmp)
            Space: O(mp + mn)

        Args:
            mat (Matrix): The matrix to be multiplied with the matrix.

        Returns:
            Matrix: A new Matrix resulting from the matrix multiplication.
        """

        m_rows, m_columns = mat.get_shape() # Space and time complexity of O(1).
        rows, columns = self.get_shape() # Space and time complexity of O(1).

        if columns != m_rows: # Raise error if number of columns in the first matrix is different than the number of rows in the second one.
            raise ValueError("Matrix A columns must match Matrix B rows for multiplication.")

        result = [[0] * m_columns for _ in range(rows)] # Creating table of shape m rows and p columns.
        for n in range(columns): # Iterate through columns n times.
            for m in range(rows): # Iterate through rows m times.
                for p in range(m_columns): # Iterate through second matrix columns p times.
                    result[m][p] += self[m][n] * mat[n][p]

        return Matrix(result)

    def trace(self) -> float:
        """
        Computes the trace of a square matrix.

        Complexity:
            Time: O(n)
            Space: O(1)

        Returns:
            float: The trace value.
        """
        rows, columns = self.get_shape() # Space and time complexity of O(1).

        if rows != columns: # Raise error if number of rows is different than the number of columns.
            raise ValueError("The matrix must be square to compute the trace.")

        result = 0
        for n in range(rows): # Loop through rows n times.
            result += self.data[n][n]

        return result

    def transpose(self) -> 'Matrix':
        """
        Computes the transpose of the matrix.

        Returns:
            Matrix: The transpose of the original matrix.
        """
        rows, columns = self.get_shape()

        result = [[0] * rows for _ in range(columns)]
        for n in range(columns):
            for m in range(rows):
                result[n][m] = self[m][n]

        return Matrix(result)

    def row_echelon(self) -> 'Matrix':
        """
        Compute the row echelon form of a matrix.

        Returns:
            Matrix: The row echelon form of the matrix.
        """

        matrix = self.data.copy()
        rows, columns = self.get_shape()

        lead = 0
        for r in range(rows):
            if lead >= columns:
                break

            pivot = r
            while matrix[pivot][lead] == 0:
                pivot += 1
                if pivot == rows:
                    pivot = r
                    lead += 1
                    if columns == lead:
                        return Matrix(matrix)

            matrix[pivot], matrix[r] = matrix[r], matrix[pivot]

            if matrix[r][lead] != 0:
                reciprocal = 1.0 / matrix[r][lead]
                matrix[r] = [elem * reciprocal for elem in matrix[r]]

            for i in range(rows):
                if i != r:
                    factor = matrix[i][lead]
                    matrix[i] = [elem - factor * matrix[r][idx] for idx, elem in enumerate(matrix[i])]

            lead += 1
        return Matrix(matrix)

    def determinant(self) -> float:
        """
        Compute the determinant of a square matrix.

        Returns:
            float: Determinant of the square matrix.
        """

        def two_by_two(matrix) -> float:
            """
            Computes determinant for a 2x2 matrix

            Args:
                matrix (list[list[float]]): The matrix to compute the determinant for.

            Returns:
                float: Determinant of the 2x2 matrix.
            """

            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        def three_by_three(matrix):
            """
            Computes determinant for a 3x3 matrix

            Args:
                matrix (list[list[float]]): The matrix to compute the determinant for.

            Returns:
                float: Determinant of the 3x3 matrix.
            """

            return (
                matrix[0][0] * two_by_two([
                    [matrix[1][1], matrix[1][2]],
                    [matrix[2][1], matrix[2][2]]
                ])
                - matrix[0][1] * two_by_two([
                    [matrix[1][0], matrix[1][2]],
                    [matrix[2][0], matrix[2][2]]
                ])
                + matrix[0][2] * two_by_two([
                    [matrix[1][0], matrix[1][1]],
                    [matrix[2][0], matrix[2][1]]
                ])
            )

        def four_by_four(matrix) -> float:
            """
            Computes determinant for a 4x4 matrix

            Args:
                matrix (list[list[float]]): The matrix to compute the determinant for.

            Returns:
                float: Determinant of the 4x4 matrix.
            """

            return (
                matrix[0][0] * three_by_three([
                    [matrix[1][1], matrix[1][2], matrix[1][3]],
                    [matrix[2][1], matrix[2][2], matrix[2][3]],
                    [matrix[3][1], matrix[3][2], matrix[3][3]]
                ])
                - matrix[0][1] * three_by_three([
                    [matrix[1][0], matrix[1][2], matrix[1][3]],
                    [matrix[2][0], matrix[2][2], matrix[2][3]],
                    [matrix[3][0], matrix[3][2], matrix[3][3]]
                ])
                + matrix[0][2] * three_by_three([
                    [matrix[1][0], matrix[1][1], matrix[1][3]],
                    [matrix[2][0], matrix[2][1], matrix[2][3]],
                    [matrix[3][0], matrix[3][1], matrix[3][3]]
                ])
                - matrix[0][3] * three_by_three([
                    [matrix[1][0], matrix[1][1], matrix[1][2]],
                    [matrix[2][0], matrix[2][1], matrix[2][2]],
                    [matrix[3][0], matrix[3][1], matrix[3][2]]
                ])
            )

        rows, columns = self.get_shape()

        if rows != columns:
            raise ValueError("The matrix must be square to compute the determinant.")

        if rows > 4:
            raise ValueError("The dimension of the matrix must not be greater than 4x4.")

        determinant_functions = {
            2: two_by_two,
            3: three_by_three,
            4: four_by_four
        }

        return determinant_functions[rows](self)

    def inverse(self) -> 'Matrix':
        """
        Compute the inverse of a square matrix.

        Returns:
            Matrix: The inverse matrix.
        """
        rows, columns = self.get_shape()

        if rows != columns:
            raise ValueError("The matrix must be square to compute the determinant.")

        matrix = [row[:] + [int(i == j) for j in range(rows)] for i, row in enumerate(self)]

        lead = 0
        for r in range(rows):
            if lead >= columns:
                break

            pivot = r
            while matrix[pivot][lead] == 0:
                pivot += 1
                if pivot == rows:
                    pivot = r
                    lead += 1
                    if columns == lead:
                        return Matrix([row[rows:] for row in matrix])

            matrix[pivot], matrix[r] = matrix[r], matrix[pivot]

            if matrix[r][lead] != 0:
                reciprocal = 1.0 / matrix[r][lead]
                matrix[r] = [elem * reciprocal for elem in matrix[r]]

            for i in range(rows):
                if i != r:
                    factor = matrix[i][lead]
                    matrix[i] = [elem - factor * matrix[r][idx] for idx, elem in enumerate(matrix[i])]

            lead += 1
        return Matrix([row[rows:] for row in matrix])

    def rank(self) -> int:
        """
        Computes the rank of the matrix.

        Returns:
            int: The rank of the matrix.
        """

        row_echelon = self.row_echelon()
        return sum(1 for row in row_echelon if any(row))
