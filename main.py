import secrets as s


def random_a():
    return s.randbelow(6)


def random_b():
    return s.randbelow(9)


def a_from_b():
    temp_storage = 0
    for i in range(1, 5, 1):
        temp_storage += random_b()
    return temp_storage % 6


def b_from_a():
    temp_storage = 0
    for i in range(1, 9, 1):
        temp_storage += random_a()
    return temp_storage % 9


def main():
    a_from_b_storage = []
    b_from_a_storage = []
    for x in range(0, 10000000):
        temp_a = b_from_a()
        temp_b = a_from_b()
        a_from_b_storage.append(temp_b)
        b_from_a_storage.append(temp_a)
    print("\na from b")

    for x in range(0, 6):
        print(x, a_from_b_storage.count(x), "%", a_from_b_storage.count(x)/100000)

    print("\nb from a")
    for x in range(0, 9):
        print(x, b_from_a_storage.count(x), "%", b_from_a_storage.count(x)/100000)


if __name__ == "__main__":
    main()