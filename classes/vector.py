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

    def norm_1(self) -> float:
        """
        The Manhattan norm (L1 norm), is a way to measure the magnitude or size of a vector in a vector space.
        It is calculated by summing the absolute values of the components of the vector.

        Returns:
            float: The L1 norm.
        """
        res = 0

        for x in self.data:
            res += abs(x)

        return res

    def norm(self) -> float:
        """
        The Euclidean norm (L2 norm), is a way to measure the magnitude or size of a vector in a vector space.
        It calculates the length of a vector using a square root of the sum of the squares of its individual components.

        Returns:
            float: The L2 norm.
        """

        res = 0
        for x in self.data:
            res += pow(x, 2)

        return res ** 0.5

    def norm_inf(self) -> float:
        """
        The supremum norm (L∞ norm) is a way to measure the magnitude or size of a vector in a vector space.
        It calculates the maximum absolute value among the components of a vector.

        Returns:
            float: The L∞ norm.
        """

        return max([abs(x) for x in self.data])
