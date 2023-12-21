from classes.vector import Vector

def cross_product(u: Vector, v: Vector) -> Vector:
    """
    Calculate the cross product of two 3-dimensional vectors.

    Args:
        u (Vector): First vector.
        v (Vector): Second vector.

    Raises:
        ValueError: If the input vectors are not 3-dimensional.

    Returns:
        Vector: The resulting vector from the cross product operation.
    """

    if u.get_size() != 3 or v.get_size() != 3:
        raise ValueError("Vectors must be 3-dimensional.")

    return Vector([
        u.data[1] * v.data[2] - v.data[1] * u.data[2],
        u.data[2] * v.data[0] - v.data[2] * u.data[0],
        u.data[0] * v.data[1] - v.data[0] * u.data[1]
    ])
