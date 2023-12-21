from typing import Union
from classes.matrix import Matrix
from classes.vector import Vector

def lerp(u: Union[float, Vector, Matrix], v: Union[float, Vector, Matrix], t: float) -> Union[float, Vector, Matrix]:
    if t < 0 or t > 1:
        raise ValueError("Scaler must be between 0 and 1")

    if u.__class__ in (int, float) and v.__class__ in (int, float):
        return round((1 - t) * u + t * v, 1)

    if u.__class__ == Vector and v.__class__ == Vector:
        u_size = u.get_size()
        v_size = v.get_size()

        if u_size != v_size:
            raise ValueError("Vectors must be of the same size.")

        return Vector([
            round((1 - t) * a + t * b, 1)
            for a, b in zip(u, v)
        ])

    if u.__class__ == Matrix and v.__class__ == Matrix:
        u_rows, u_columns = u.get_shape()
        v_rows, v_columns = v.get_shape()

        if u_rows != v_rows or u_columns != v_columns:
            raise ValueError("Matrix must be of the same size.")

        return Matrix([
            [
                round((1 - t) * a + t * b, 1)
                for a, b in zip(row_u, row_v)
            ] for row_u, row_v in zip(u, v)
        ])

    return TypeError(f"Cannot compute linear interpolation of {type(u)} and {type(v)}.")