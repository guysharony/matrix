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
            assert data.__class__ == list, \
                "matrix data must be of type list of list"

            assert all(len(row) == len(data[0]) for row in data), \
                "matrix rows must be the same size"

            assert all(all(value.__class__ in (float, int) for value in row) for row in data), \
                "matrix values must be of type float or int"

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
        assert self.rows == v.rows and self.columns == v.columns, \
            "Cannot add matrixs of different size."

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
        assert self.rows == v.rows and self.columns == v.columns, \
            "Cannot subtract matrixs of different size."

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
        self.data = [[x * k for x in a] for a in self.data]
        return self
