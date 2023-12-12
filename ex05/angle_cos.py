from classes.vector import Vector

def angle_cos(u: Vector, v: Vector) -> float:
    """
    Calculate the cosine similarity between two vectors.

    Args:
        u (Vector): First vector.
        v (Vector): Second vector.

    Returns:
        float: Cosine similarity between the input vectors.
    """
    if all(value == 0 for value in v.data) or all(value == 0 for value in u.data):
        raise ValueError("A vector cannot be null.")

    if u.length != v.length:
        raise ValueError("Vectors must have the same size.")

    return round(u.dot(v) / (u.norm() * v.norm()), 8)