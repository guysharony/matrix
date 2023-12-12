from typing import Union
from classes.matrix import Matrix
from classes.vector import Vector

def lerp(u: Union[float, Vector, Matrix], v: Union[float, Vector, Matrix], t: float) -> Union[float, Vector, Matrix]:
    if t < 0 or t > 1:
        raise ValueError("Scaler must be between 0 and 1")

    if u.__class__ in (int, float) and v.__class__ in (int, float):
        return round((1 - t) * u + t * v, 1)

    if u.__class__ == Vector and v.__class__ == Vector:
        if u.length != v.length:
            raise ValueError("Vectors must be of the same size")

        return Vector([
            round((1 - t) * a + t * b, 1)
            for a, b in zip(u.data, v.data)
        ])

    if u.__class__ == Matrix and v.__class__ == Matrix:
        if u.rows != v.rows or u.columns != v.columns:
            raise ValueError("Matrix must be of the same size")

        return Matrix([
            [
                round((1 - t) * a + t * b, 1)
                for a, b in zip(row_a, row_b)
            ] for row_a, row_b in zip(u.data, v.data)
        ])

    return TypeError(f"Cannot compute linear interpolation of {type(u)} and {type(v)}.")