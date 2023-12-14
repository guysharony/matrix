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

        if self.columns == vec.length:
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
