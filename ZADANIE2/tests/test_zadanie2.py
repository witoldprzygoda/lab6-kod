import weakref

import pytest

from ZADANIE2.zadanie2 import Rejestr


class Foo:
    pass


def test_zywe_obiekty_w_kolejnosci_dodania():
    rejestr = Rejestr()
    a, b = Foo(), Foo()
    rejestr.dodaj(a)
    rejestr.dodaj(b)
    wynik = rejestr.zywe()
    assert len(wynik) == 2
    assert wynik[0] is a
    assert wynik[1] is b


def test_usuniety_obiekt_znika_z_rejestru():
    rejestr = Rejestr()
    a, b, c = Foo(), Foo(), Foo()
    for obiekt in (a, b, c):
        rejestr.dodaj(obiekt)
    del b
    wynik = rejestr.zywe()
    assert len(wynik) == 2
    assert wynik[0] is a
    assert wynik[1] is c


def test_rejestr_nie_utrzymuje_obiektow():
    rejestr = Rejestr()
    a = Foo()
    rejestr.dodaj(a)
    obserwator = weakref.ref(a)
    del a
    assert obserwator() is None
    assert rejestr.zywe() == []


def test_typ_bez_slabych_referencji():
    rejestr = Rejestr()
    with pytest.raises(TypeError):
        rejestr.dodaj(5)
    with pytest.raises(TypeError):
        rejestr.dodaj([1, 2])


def test_zywe_zwraca_nowa_liste():
    rejestr = Rejestr()
    a = Foo()
    rejestr.dodaj(a)
    pierwsza = rejestr.zywe()
    pierwsza.clear()
    assert rejestr.zywe() == [a]
