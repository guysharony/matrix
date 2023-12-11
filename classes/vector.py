class Vector:
    def __init__(self, data: list[float]):
        try:
            assert len(data) != 0, \
                "vector cannot be empty"

            assert all(x.__class__ in (int, float) for x in data), \
                "All elements in vector must be of type int or float"
            
            self.data = data
        except Exception as err:
            print(f'error: {err}')

    def __str__(self) -> str:
        return str(self.data)

    def add(self, v: 'Vector') -> 'Vector':
        assert len(self.data) == len(v.data), \
            "Cannot add vectors of different size."

        self.data = [a + b for a, b in zip(self.data, v.data)]
        return self

    def sub(self, v: 'Vector') -> 'Vector':
        assert len(self.data) == len(v.data), \
            "Cannot subtract vectors of different size."

        self.data = [a - b for a, b in zip(self.data, v.data)]
        return self

    def scl(self, k: float) -> 'Vector':
        self.data = [a * k for a in self.data]
        return self