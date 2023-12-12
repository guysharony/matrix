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
    return round(u.dot(v) / (u.norm() * v.norm()), 8)