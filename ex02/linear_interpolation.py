from typing import Union
from classes.matrix import Matrix
from classes.vector import Vector

def lerp(u: Union[float, Vector, Matrix], v: Union[float, Vector, Matrix], t: float) -> Union[float, Vector, Matrix]:
    """
    Performs linear interpolation between two values, vectors, or matrices based on a scalar value 't'.

    Complexity:
        Time: O(n)
        Space: O(n)

    Args:
        u (Union[float, Vector, Matrix]): First value, vector, or matrix for interpolation.
        v (Union[float, Vector, Matrix]): Second value, vector, or matrix for interpolation.
        t (float): Scalar value between 0 and 1 determining the interpolation ratio.

    Returns:
        Union[float, Vector, Matrix]: The interpolated value, vector, or matrix based on 't'.
    """

    if t < 0 or t > 1: # Condition of complexity of O(1).
        raise ValueError("Scaler must be between 0 and 1")

    if u.__class__ in (int, float) and v.__class__ in (int, float): # Condition of complexity of O(1).
        return round((1 - t) * u + t * v, 1) # Complexity of O(1) (operation).

    if u.__class__ == Vector and v.__class__ == Vector: # Condition of complexity of O(1).
        u_size = u.get_size() # Space and time complexity of O(1).
        v_size = v.get_size() # Space and time complexity of O(1).

        if u_size != v_size: # Space and time complexity of O(1).
            raise ValueError("Vectors must be of the same size.")

        return Vector([
            round((1 - t) * a + t * b, 1)
            for a, b in zip(u, v)
        ]) # Loop u and v so complexity of O(n).

    if u.__class__ == Matrix and v.__class__ == Matrix: # Condition of complexity of O(1).
        u_rows, u_columns = u.get_shape() # Space and time complexity of O(1).
        v_rows, v_columns = v.get_shape() # Space and time complexity of O(1).

        if u_rows != v_rows or u_columns != v_columns: # Condition of complexity of O(1).
            raise ValueError("Matrix must be of the same size.")

        return Matrix([
            [
                round((1 - t) * a + t * b, 1)
                for a, b in zip(row_u, row_v)
            ] for row_u, row_v in zip(u, v)
        ]) # Complexity of O(n) as "The 'n' in complexity is the dimension of the vector/matrix".

    return TypeError(f"Cannot compute linear interpolation of {type(u)} and {type(v)}.")