# Lab. 6 – klasy i metody specjalne

Pliki początkowe zadań. Uzupełniamy pliki `zadanien.py`; nazw klas, metod i plików z katalogów `tests` nie zmieniamy.

| Zadanie | Plik | Temat |
|---|---|---|
| 1 | `ZADANIE1/zadanie1.py` | Licznik obiektów klasy `Bug` |
| 2 | `ZADANIE2/zadanie2.py` | Rejestr żywych obiektów |
| 3 | `ZADANIE3/zadanie3.py` | Odejmowanie i porównanie |
| 4 | `ZADANIE4/zadanie4.py` | Plansza do kółka i krzyżyka |

## Środowisko i testy

Polecenia wydajemy w katalogu głównym repozytorium.

```bash title="Terminal"
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

W Windows środowisko aktywuje polecenie `.venv\Scripts\Activate.ps1`. Jedno zadanie sprawdza np. `python -m pytest ZADANIE1`.
