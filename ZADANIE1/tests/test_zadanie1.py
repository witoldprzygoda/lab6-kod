from ZADANIE1.zadanie1 import Bug


def test_klasa_ma_docstring():
    assert Bug.__doc__ is not None
    assert Bug.__doc__.strip() != ""


def test_licznik_jest_atrybutem_klasy():
    assert "licznik" in vars(Bug)
    assert isinstance(Bug.licznik, int)


def test_init_zwieksza_licznik_i_nadaje_id():
    poczatek = Bug.licznik
    b = Bug()
    assert Bug.licznik == poczatek + 1
    assert b.id == Bug.licznik
    assert "licznik" not in vars(b)
    del b


def test_kolejne_obiekty_maja_kolejne_id():
    a = Bug()
    b = Bug()
    assert b.id == a.id + 1
    del a, b


def test_str(capsys):
    b = Bug()
    assert str(b) == f"Licznik: {Bug.licznik}, id: {b.id}"
    print(b)
    assert capsys.readouterr().out == f"Licznik: {Bug.licznik}, id: {b.id}\n"
    del b


def test_del_wypisuje_komunikat_i_zmniejsza_licznik(capsys):
    poczatek = Bug.licznik
    b = Bug()
    numer = b.id
    capsys.readouterr()
    del b
    assert capsys.readouterr().out == f"Koniec, licznik: {poczatek + 1}, id: {numer}\n"
    assert Bug.licznik == poczatek


def test_obiekt_z_druga_nazwa_zyje_dalej(capsys):
    poczatek = Bug.licznik
    b = Bug()
    druga = b
    del b
    assert Bug.licznik == poczatek + 1
    assert capsys.readouterr().out == ""
    del druga
    assert Bug.licznik == poczatek
