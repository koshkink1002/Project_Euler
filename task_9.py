def are_pythogorians(a: int, b: int, c: int) -> bool:
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def show_pythogorians(limit: int):
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if are_pythogorians(a, b, c):
                    print(a, b, c)


show_pythogorians(20)
