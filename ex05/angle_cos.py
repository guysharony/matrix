from classes.vector import Vector

def angle_cos(u: Vector, v: Vector) -> float:
    """
    Calculate the cosine similarity between two vectors.

    Complexity:
        Time: O(n)
        Space: O(1)

    Args:
        u (Vector): First vector.
        v (Vector): Second vector.

    Returns:
        float: Cosine similarity between the input vectors.
    """
    if all(value == 0 for value in v.data) or all(value == 0 for value in u.data): # Loop through v and u O(n)
        raise ValueError("A vector cannot be null.")

    if u.get_size() != v.get_size(): # Space and time complexity of O(1).
        raise ValueError("Vectors must have the same size.")

    return round(u.dot(v) / (u.norm() * v.norm()), 9) # Operations using functions of complexity O(n) so time complexity of O(n)