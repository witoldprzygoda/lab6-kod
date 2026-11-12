import pytest

from ZADANIE4.zadanie4 import TicTacToeBoard


def test_pusta_plansza():
    assert str(TicTacToeBoard()) == ". . .\n. . .\n. . ."


def test_odczyt_pustego_pola():
    plansza = TicTacToeBoard()
    assert plansza[0, 0] == "."
    assert plansza[2, 1] == "."


def test_zapis_i_odczyt():
    plansza = TicTacToeBoard()
    plansza[0, 0] = "X"
    plansza[1, 1] = "O"
    plansza[2, 2] = "X"
    assert plansza[0, 0] == "X"
    assert plansza[1, 1] == "O"
    assert plansza[2, 2] == "X"
    assert str(plansza) == "X . .\n. O .\n. . X"


def test_wiersz_i_kolumna_nie_sa_zamienione():
    plansza = TicTacToeBoard()
    plansza[0, 2] = "O"
    assert plansza[0, 2] == "O"
    assert plansza[2, 0] == "."
    assert str(plansza) == ". . O\n. . .\n. . ."


def test_zapis_zmienia_tylko_jedno_pole():
    plansza = TicTacToeBoard()
    plansza[1, 0] = "X"
    assert str(plansza) == ". . .\nX . .\n. . ."


def test_osobne_plansze_sa_niezalezne():
    pierwsza, druga = TicTacToeBoard(), TicTacToeBoard()
    pierwsza[1, 1] = "X"
    assert druga[1, 1] == "."


def test_indeks_poza_plansza():
    plansza = TicTacToeBoard()
    with pytest.raises(IndexError):
        plansza[3, 0]
    with pytest.raises(IndexError):
        plansza[0, 3] = "X"
