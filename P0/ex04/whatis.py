import sys


def main():
    try:
        len_args = len(sys.argv[1:])

        if len_args == 0:
            return
        elif len_args > 1:
            raise AssertionError("more than one argument is provided")
        try:
            value = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if value % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
