class Bug:
    licznik = 0

    def __init__(self):
        pass  # tu kod

    def __del__(self):
        pass  # tu kod

    def __str__(self):
        pass  # tu kod


if __name__ == "__main__":
    bugs = []
    for i in range(3):
        bugs.append(Bug())
        print(bugs[-1])
    del bugs
