def list_from_string(long_string):
    return long_string.split(" ")


def list_from_letters(long_string):
    return [letter for letter in long_string if letter != " "]


def main():
    long_string = "To jest testowy String taki jak najdłuższy, bla bla bla bla"
    print(list_from_string(long_string))
    s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
    print(eval(s))
    print(list_from_letters(long_string))


if __name__ == "__main__":
    main()
