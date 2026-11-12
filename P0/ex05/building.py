import sys
import string


def main():
    try:
        len_args = len(sys.argv[1:])

        if len_args == 0 or not sys.argv[1]:
            print("What is the text to count?:")
            text = sys.stdin.readline()
        elif len_args > 1:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]

        print(f"The text contains {len(text)} characters:")
        print(f"{sum(1 for c in text if c.isupper())} upper letters")
        print(f"{sum(1 for c in text if c.islower())} lower letters")
        ponctuation = sum(1 for c in text if c in string.punctuation)
        print(f"{ponctuation} ponctuation marks")
        print(f"{sum(1 for c in text if c.isspace())} spaces")
        print(f"{sum(1 for c in text if c.isdigit())} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
