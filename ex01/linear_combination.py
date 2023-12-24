from classes.vector import Vector


def linear_combination(u: list[Vector], coefs: list[float]) -> Vector:
    """
    Computes the linear combination of vectors.

    Complexity:
        Time: O(n)
        Space: O(n)

    Args:
        u (list[Vector]): A list of Vector objects.
        coefs (list[float]): A list of coefficients.

    Returns:
        Vector: A Vector representing the linear combination of vectors in u with the given coefficients.
    """

    if u.__class__ != list or not all(vector.__class__ == Vector for vector in u):
        raise TypeError("u must be a list of Vector.")

    if coefs.__class__ != list or not all(coef.__class__ in (float, int) for coef in coefs):
        raise TypeError("coefs must be a list of int or float.")

    if len(u) != len(coefs):
        raise ValueError("u and coefs must be of the same size.")

    result_vector = Vector([0.0] * u[0].get_size()) # Space complexity of O(n)
    for vector, coef in zip(u, coefs): # Void as "The 'n' in complexity is the dimension of the vector/matrix".
        result_vector.add(vector.scl(coef)) # Complexity of O(n)

    return result_vector