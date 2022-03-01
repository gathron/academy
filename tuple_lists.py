def get_tuple():
    tuple1 = tuple()
    for x in range(5, 10, 2):
        tuple1 = tuple1 + (x,)
    return tuple1


def main():
    print(get_tuple())


if __name__ == "__main__":
    main()
