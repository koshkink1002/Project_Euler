def create_list_with_numbers(limit: int) -> list[int]:
    numbers: list[int] = []
    for number in range(1, limit):
        if number % 3 == 0 or number % 5 == 0:
            numbers.append(number)
    return numbers


def find_sum(integers: list[int]) -> int:
    summa = 0
    for integer in integers:
        summa = summa + integer
    return summa


numbers: list[int] = create_list_with_numbers(1000)
print(numbers)

summa = find_sum(numbers)
print(summa)
