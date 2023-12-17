from classes.vector import Vector


class Matrix:
    """
    A class to represent a matrix.
    """

    def __init__(self, data: list[list[float]]):
        """
        Initializes a matrix with the provided data.

        Args:
            data (list[list[float]]): A list containing elements representing the matrix.
        """

        try:
            if data.__class__ != list:
                raise ValueError("Matrix values must be of type list of list")

            if not all(len(row) == len(data[0]) for row in data):
                raise ValueError("Matrix rows must be the same size.")

            if not all(all(value.__class__ in (float, int) for value in row) for row in data):
                raise ValueError("Matrix values must be of type float or int")

            self.data = data
            self.rows = len(data)
            self.columns = len(data[0])
        except Exception as err:
            print(f'error: {err}')

    def __str__(self) -> str:
        """
        Returns the string representation of the matrix.

        Returns:
            str: A string representation of the matrix.
        """

        return str(self.data)

    def add(self, v: 'Matrix') -> 'Matrix':
        """
        Adds another matrix to this matrix.

        Args:
            v (Matrix): Another matrix to be added.

        Returns:
            Matrix: This matrix after addition.
        """

        if self.rows != v.rows or self.columns != v.columns:
            raise ValueError("Matrices must have the same dimensions for addition.")

        self.data = [[x + y for x, y in zip(a, b)] for a, b in zip(self.data, v.data)]
        return self

    def sub(self, v: 'Matrix') -> 'Matrix':
        """
        Subtract another matrix from this matrix.

        Args:
            v (Matrix): Another matrix to be subtracted.

        Returns:
            Matrix: This matrix after subtraction.
        """

        if self.rows != v.rows or self.columns != v.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        self.data = [[x - y for x, y in zip(a, b)] for a, b in zip(self.data, v.data)]
        return self

    def scl(self, k: float) -> 'Matrix':
        """
        Scales this matrix by a factor.

        Args:
            k (float): The scaler.

        Returns:
            Matrix: This matrix after scaling.
        """

        self.data = [[x * k for x in row] for row in self.data]
        return self

    def mul_vec(self, vec: 'Vector') -> 'Vector':
        """
        Multiplies the matrix by a vector.

        Args:
            vec (Vector): The vector to be multiplied with the matrix.

        Returns:
            Vector: A new Vector resulting from the matrix-vector multiplication.
        """

        if self.columns != vec.length:
            raise ValueError("Matrix columns must match vector length for multiplication.")

        result = [0] * vec.length

        for n in range(self.columns):
            for m in range(self.rows):
                result[m] += self.data[m][n] * vec.data[n]

        return Vector(result)

    def mul_mat(self, mat: 'Matrix') -> 'Matrix':
        """
        Multiplies two matrices.

        Args:
            mat (Matrix): The matrix to be multiplied with the matrix.

        Returns:
            Matrix: A new Matrix resulting from the matrix multiplication.
        """

        if self.columns != mat.rows:
            raise ValueError("Matrix A columns must match Matrix B rows for multiplication.")

        result = [[0] * mat.columns for _ in range(self.rows)]
        for n in range(self.columns):
            for m in range(self.rows):
                for p in range(mat.columns):
                    result[m][p] += self.data[m][n] * mat.data[n][p]

        return Matrix(result)

    def trace(self) -> float:
        """
        Computes the trace of a square matrix.
    
        Returns:
            float: The trace value.
        """

        if self.columns != self.rows:
            raise ValueError("The matrix must be square to compute the trace.")

        result = 0
        for n in range(self.rows):
            result += self.data[n][n]

        return result

    def transpose(self) -> 'Matrix':
        """
        Computes the transpose of the matrix.

        Returns:
            Matrix: The transpose of the original matrix.
        """

        result = [[0] * self.rows for _ in range(self.columns)]
        for n in range(self.columns):
            for m in range(self.rows):
                result[n][m] = self.data[m][n]

        return Matrix(result)

    def row_echelon(self) -> 'Matrix':
        """
        Compute the row echelon form of a matrix.

        Returns:
            Matrix: The row echelon form of the matrix.
        """

        matrix = self.data.copy()

        lead = 0
        for r in range(self.rows):
            if lead >= self.columns:
                break

            pivot = r
            while matrix[pivot][lead] == 0:
                pivot += 1
                if pivot == self.rows:
                    pivot = r
                    lead += 1
                    if self.columns == lead:
                        return Matrix(matrix)

            matrix[pivot], matrix[r] = matrix[r], matrix[pivot]

            if matrix[r][lead] != 0:
                reciprocal = 1.0 / matrix[r][lead]
                matrix[r] = [elem * reciprocal for elem in matrix[r]]

            for i in range(self.rows):
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

        if self.rows != self.columns:
            raise ValueError("The matrix must be square to compute the determinant.")

        if self.rows > 4:
            raise ValueError("The dimension of the matrix must not be greater than 4x4.")

        determinant_functions = {
            2: two_by_two,
            3: three_by_three,
            4: four_by_four
        }

        return determinant_functions[self.rows](self.data)

    def inverse(self) -> 'Matrix':
        return Matrix()