def get_tuple():
    tuple1 = tuple()
    for x in range(5, 10, 2):
        tuple1 = tuple1 + (x,)
    return tuple1


def get_list_reversed(my_range, my_step):
    list1 = []
    for x in range(my_range, 0, -my_step):
        list1.append(x)
    return list1


def main():
    print(get_tuple())
    print(get_list_reversed(10, 2))


if __name__ == "__main__":
    main()
