def are_pythagorians(a: int, b: int, c: int) -> bool:
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def show_pythagorians(limit: int):
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if are_pythagorians(a, b, c):
                    print(a, b, c)


show_pythagorians(20)
