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
            if data.__class__ != list:
                raise ValueError("Vector data must be of type list")

            if len(data) == 0:
                raise ValueError("Vector cannot be empty")

            if not all(x.__class__ in (int, float) for x in data):
                raise ValueError("Vector elements must be of type int or float")

            self.data = data
        except Exception as err:
            print(f'error: {err}')

    def __str__(self) -> str:
        """
        Returns the string representation of the vector.

        Returns:
            str: A string representation of the vector.
        """

        return str(self.data)

    def __getitem__(self, index: int) -> float:
        return self.data[index]

    def get_size(self) -> int:
        """
        Retrieve the length of the vector.

        Returns:
            int: The length of the vector.
        """
        return len(self.data)

    def add(self, v: 'Vector') -> 'Vector':
        """
        Adds another vector to this vector.

        Args:
            v (Vector): Another vector to be added.

        Returns:
            Vector: This vector after addition.
        """

        if self.length != v.length:
            raise ValueError("Vectors must have the same length for addition.")

        self.data = [a + b for a, b in zip(self, v)]
        return self

    def sub(self, v: 'Vector') -> 'Vector':
        """
        Subtract another vector from this vector.

        Args:
            v (Vector): Another vector to be subtracted.

        Returns:
            Vector: This vector after subtraction.
        """

        if self.length != v.length:
            raise ValueError("Vectors must have the same length for subtraction.")

        self.data = [a - b for a, b in zip(self, v)]
        return self

    def scl(self, k: float) -> 'Vector':
        """
        Scales this vector by a factor.

        Args:
            k (float): The scaler.

        Returns:
            Vector: This vector after scaling.
        """

        self.data = [a * k for a in self]
        return self

    def dot(self, v: 'Vector') -> float:
        """
        Computes the dot product of two vectors.

        Args:
            v (Vector): The second Vector to perform the dot product.

        Returns:
            float: The dot product value.
        """

        if self.length != v.length:
            raise ValueError("Vectors must have the same length for dot product.")

        result = 0
        for a, b in zip(self, v):
            result += a * b

        return result

    def norm_1(self) -> float:
        """
        The Manhattan norm (L1 norm), is a way to measure the magnitude or size of a vector in a vector space.
        It is calculated by summing the absolute values of the components of the vector.

        Returns:
            float: The L1 norm.
        """

        result = 0
        for x in self:
            result += abs(x)

        return result

    def norm(self) -> float:
        """
        The Euclidean norm (L2 norm), is a way to measure the magnitude or size of a vector in a vector space.
        It calculates the length of a vector using a square root of the sum of the squares of its individual components.

        Returns:
            float: The L2 norm.
        """

        result = 0
        for x in self:
            result += pow(x, 2)

        return result ** 0

    def norm_inf(self) -> float:
        """
        The supremum norm (L∞ norm) is a way to measure the magnitude or size of a vector in a vector space.
        It calculates the maximum absolute value among the components of a vector.

        Returns:
            float: The L∞ norm.
        """

        return max([abs(x) for x in self])
