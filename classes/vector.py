class Vector:
    """
    A class to represent a vector.
    """

    def __init__(self, data: list[float]):
        """
        Initializes a vector with the provided data.

        Args:
            data (list[float]): A list containing elements representing the vector.
        """

        try:
            assert data.__class__ == list, \
                "vector data must be of type list"

            assert len(data) != 0, \
                "vector cannot be empty"

            assert all(x.__class__ in (int, float) for x in data), \
                "All elements in vector must be of type int or float"

            self.data = data
            self.length = len(data)
        except Exception as err:
            print(f'error: {err}')

    def __str__(self) -> str:
        """
        Returns the string representation of the vector.

        Returns:
            str: A string representation of the vector.
        """
        return str(self.data)

    def add(self, v: 'Vector') -> 'Vector':
        """
        Adds another vector to this vector.

        Args:
            v (Vector): Another vector to be added.

        Returns:
            Vector: This vector after addition.
        """
        assert self.length == v.length, \
            "Cannot add vectors of different size."

        self.data = [a + b for a, b in zip(self.data, v.data)]
        return self

    def sub(self, v: 'Vector') -> 'Vector':
        """
        Subtract another vector from this vector.

        Args:
            v (Vector): Another vector to be subtracted.

        Returns:
            Vector: This vector after subtraction.
        """
        assert self.length == v.length, \
            "Cannot subtract vectors of different size."

        self.data = [a - b for a, b in zip(self.data, v.data)]
        return self

    def scl(self, k: float) -> 'Vector':
        """
        Scales this vector by a factor.

        Args:
            k (float): The scaler.

        Returns:
            Vector: This vector after scaling.
        """
        self.data = [a * k for a in self.data]
        return self

    def dot(self, v: 'Vector') -> float:
        assert self.length == v.length, \
            "Cannot subtract vectors of different size."

        res = 0
        for a, b in zip(self.data, v.data):
            res += a * b

        return res
