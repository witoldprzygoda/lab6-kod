import weakref


class Rejestr:
    """Rejestr obiektów, który nie utrzymuje ich w pamięci."""

    def __init__(self):
        self._referencje = []

    def dodaj(self, obiekt):
        pass  # tu kod

    def zywe(self):
        pass  # tu kod


class Foo:
    pass


if __name__ == "__main__":
    rejestr = Rejestr()
    a, b = Foo(), Foo()
    rejestr.dodaj(a)
    rejestr.dodaj(b)
    print(len(rejestr.zywe()))
    del a
    print(len(rejestr.zywe()))
