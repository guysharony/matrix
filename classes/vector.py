class Vector:
    """
    A class to represent a vector.
    """

    def __init__(self, data: list[float]):
        """
        Initializes a vector with the provided data.

        Complexity:
            Time: O(n)
            Space: O(1)

        Args:
            data (list[float]): A list containing elements representing the vector.
        """

        try:
            if data.__class__ != list: # Operations have complexity of O(1)
                raise ValueError("Vector data must be of type list")

            if len(data) == 0: # Operations have complexity of O(1)
                raise ValueError("Vector cannot be empty")

            if not all(x.__class__ in (int, float) for x in data): # Complexity of O(n)
                raise ValueError("Vector elements must be of type int or float")

            self.data = data # Complexity of O(n)
        except Exception as err:
            print(f'error: {err}')

    def __str__(self) -> str:
        """
        Returns the string representation of the vector.

        Complexity:
            Time: O(n)
            Space: O(n)

        Returns:
            str: A string representation of the vector.
        """

        return str(self.data)

    def __getitem__(self, index: int) -> float:
        """
        Retrieve an element from the data list by index.

        Complexity:
            Time: O(1)
            Space: O(1)

        Args:
            index (int): The index of the element to retrieve.

        Returns:
            float: The element from the data list at the specified index.
        """
        return self.data[index]

    def get_size(self) -> int:
        """
        Retrieve the length of the vector.

        Complexity:
            Time: O(1)
            Space: O(1)

        Returns:
            int: The length of the vector.
        """
        return len(self.data)

    def add(self, v: 'Vector') -> 'Vector':
        """
        Adds another vector to this vector.

        Complexity:
            Time: O(n)
            Space: O(n)

        Args:
            v (Vector): Another vector to be added.

        Returns:
            Vector: This vector after addition.
        """

        size = self.get_size() # Space and time complexity of O(1).
        v_size = v.get_size() # Space and time complexity of O(1).

        if size != v_size: # Raise error if vectors have different size.
            raise ValueError("Vectors must have the same length for addition.")

        self.data = [a + b for a, b in zip(self.data, v)] # Loop vectors n times and creating list of n items, so time and space complexity is O(n).
        return self

    def sub(self, v: 'Vector') -> 'Vector':
        """
        Subtract another vector from this vector.

        Complexity:
            Time: O(n)
            Space: O(n)

        Args:
            v (Vector): Another vector to be subtracted.

        Returns:
            Vector: This vector after subtraction.
        """

        size = self.get_size() # Space and time complexity of O(1).
        v_size = v.get_size() # Space and time complexity of O(1).

        if size != v_size: # Raise error if vectors have different size.
            raise ValueError("Vectors must have the same length for subtraction.")

        self.data = [a - b for a, b in zip(self.data, v)] # Loop vectors n times and creating list of n items, so time and space complexity is O(n).
        return self

    def scl(self, k: float) -> 'Vector':
        """
        Scales this vector by a factor.

        Complexity:
            Time: O(n)
            Space: O(n)

        Args:
            k (float): The scaler.

        Returns:
            Vector: This vector after scaling.
        """

        self.data = [a * k for a in self.data] # Loop vector n times and creating list of n items, so time and space complexity is O(n).
        return self

    def dot(self, v: 'Vector') -> float:
        """
        Computes the dot product of two vectors.

        Complexity:
            Time: O(n)
            Space: O(1)

        Args:
            v (Vector): The second Vector to perform the dot product.

        Returns:
            float: The dot product value.
        """

        size = self.get_size() # Space and time complexity of O(1).
        v_size = v.get_size() # Space and time complexity of O(1).

        if size != v_size: # Raise error if vectors have different size.
            raise ValueError("Vectors must have the same length for dot product.")

        result = 0
        for a, b in zip(self.data, v): # Loops through vectors of same size so complexity of O(n)
            result += a * b

        return result

    def norm_1(self) -> float:
        """
        The Manhattan norm (L1 norm), is a way to measure the magnitude or size of a vector in a vector space.
        It is calculated by summing the absolute values of the components of the vector.

        Complexity:
            Time: O(n)
            Space: O(1)

        Returns:
            float: The L1 norm.
        """

        result = 0
        for x in self.data: # Loop through vector of size n so time complexity of O(n).
            result += abs(x) # abs() has complexity of O(1)

        return result

    def norm(self) -> float:
        """
        The Euclidean norm (L2 norm), is a way to measure the magnitude or size of a vector in a vector space.
        It calculates the length of a vector using a square root of the sum of the squares of its individual components.

        Complexity:
            Time: O(n)
            Space: O(1)

        Returns:
            float: The L2 norm.
        """

        result = 0
        for x in self.data: # Loop through vector n times so time complexity of O(n)
            result += x * x

        return result ** 0.5

    def norm_inf(self) -> float:
        """
        The supremum norm (L∞ norm) is a way to measure the magnitude or size of a vector in a vector space.
        It calculates the maximum absolute value among the components of a vector.

        Complexity:
            Time: O(n)
            Space: O(n)

        Returns:
            float: The L∞ norm.
        """

        abs_list = [abs(x) for x in self.data] # Recreate a list with vector's abs values so complexity of O(n).
        return max(abs_list) # max() iterate through that list to find max value so complexity of O(n).
