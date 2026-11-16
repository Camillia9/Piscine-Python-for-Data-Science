from ft_filter import ft_filter
import sys


def main():
    try:
        len_args = len(sys.argv[1:])

        if len_args != 2:
            raise AssertionError("the arguments are bad")
        try:
            words = sys.argv[1]
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = words.split()
        print(list(ft_filter(lambda word: len(word) > length, words)))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
