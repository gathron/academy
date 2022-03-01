

def list_from_string(long_string):
    return long_string.split(" ")


def main():
    long_string = "To jest testowy String taki jak najdłuższy, bla bla bla bla"
    print(list_from_string(long_string))


if __name__ == "__main__":
    main()