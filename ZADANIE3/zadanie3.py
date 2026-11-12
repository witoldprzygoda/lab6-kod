import math


class Zespolona:
    """Liczba zespolona r + i*j."""

    def __init__(self, r=0.0, i=0.0):
        self.r = float(r)
        self.i = float(i)

    def conjugate(self):
        """Sprzężenie zespolone liczby."""
        return Zespolona(self.r, -self.i)

    def argz(self):
        """Argument (faza) liczby w radianach."""
        return math.atan2(self.i, self.r)

    def __repr__(self):
        return f"Zespolona({self.r}, {self.i})"

    def __str__(self):
        znak = "+" if self.i >= 0 else "-"
        return f"{self.r} {znak} {abs(self.i)}i"

    def __add__(self, other):
        """Dodawanie: self + other."""
        if not isinstance(other, Zespolona):
            return NotImplemented
        return Zespolona(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        """Odejmowanie: self - other."""
        pass  # tu kod

    def __eq__(self, other):
        """Porównanie: self == other."""
        pass  # tu kod


if __name__ == "__main__":
    a = Zespolona(1, 2)
    b = Zespolona(3, -1)
    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a == b ?", a == b)
    print("a == Zespolona(1, 2) ?", a == Zespolona(1, 2))
