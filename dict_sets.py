def set_with_args(*args):
    my_set = set()

    for item in args:
        my_set.add(item)

    return my_set


def get_dict(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value

    return my_dict


def get_tuple_from_dict(dict1):
    list_with_keys = []
    list_with_values = []

    tuple_from_dict = (list_with_keys, list_with_values)
    print(tuple_from_dict)
    for key, values in dict1.items():
        list_with_keys.append(key)
        list_with_values.append(values)
    print(tuple_from_dict)
    return tuple_from_dict


def zip_of_lists(tuple_with_two_lists):
    return zip(tuple_with_two_lists[0], tuple_with_two_lists[1])


def main():
    # print(list(zip_of_lists(get_tuple_from_dict(get_dict(t="2", y="4")))))
    print(set_with_args(1, 2, 3, 3, 3, 2, 5))


if __name__ == "__main__":
    main()
