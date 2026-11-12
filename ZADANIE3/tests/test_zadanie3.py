import pytest

from ZADANIE3.zadanie3 import Zespolona


def test_dodawanie_dziala_od_poczatku():
    c = Zespolona(1, 2) + Zespolona(3, -1)
    assert (c.r, c.i) == (4.0, 1.0)


def test_odejmowanie():
    c = Zespolona(1, 2) - Zespolona(3, -1)
    assert isinstance(c, Zespolona)
    assert (c.r, c.i) == (-2.0, 3.0)


def test_odejmowanie_nie_zmienia_skladnikow():
    a, b = Zespolona(1, 2), Zespolona(3, -1)
    a - b
    assert (a.r, a.i, b.r, b.i) == (1.0, 2.0, 3.0, -1.0)


def test_odejmowanie_innego_typu():
    a = Zespolona(1, 2)
    assert a.__sub__(5) is NotImplemented
    with pytest.raises(TypeError):
        a - 5


def test_rownosc():
    assert Zespolona(1, 2) == Zespolona(1, 2)
    assert Zespolona(1, 2) == Zespolona(1.0, 2.0)
    assert not (Zespolona(1, 2) == Zespolona(3, -1))
    assert not (Zespolona(1, 2) == Zespolona(1, -2))


def test_nierownosc_wynika_z_rownosci():
    assert Zespolona(1, 2) != Zespolona(3, -1)
    assert not (Zespolona(1, 2) != Zespolona(1, 2))


def test_porownanie_z_innym_typem():
    a = Zespolona(1, 2)
    assert a.__eq__(5) is NotImplemented
    assert (a == 5) is False
    assert (a == "1 + 2i") is False
