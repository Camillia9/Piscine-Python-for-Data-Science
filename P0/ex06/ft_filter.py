def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which
function(item) is true.  If function is None, return the items that
are true."""
    if function is None:
        return iter([x for x in iterable if x])
    else:
        return iter([x for x in iterable if function(x)])


# def main():
#     print(ft_filter.__doc__)
#     print(list(ft_filter(lambda x: x > 2, [1, 2, 3, 4])))
#     print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))
#     print(list(ft_filter(None, [0, 1, "", "a"])))
#     print(list(filter(None, [0, 1, "", "a"])))


# if __name__ == '__main__':
#     main()
