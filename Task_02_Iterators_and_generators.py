from typing import Any, Callable, Generator, Iterator

# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries


def merge_elems(*elems: Any) -> Generator[Any, None, None]:
    """
    Flatten incoming data: non-iterables and elements from iterables (any nesting depth is supported).

    Strings are iterated character by character.
    `dict`, `bytes`, and `bytearray` are treated as non-iterable.

    :param elems: Any number of elements and any type, possibly nested.
    :return: Flattened elements one by one.
    """
    stack = list(reversed(elems))
    excluded_types = (bytes, bytearray, dict)

    while stack:
        current = stack.pop()
        if isinstance(current, str):
            for char in current:
                yield char
        elif isinstance(current, excluded_types):
            yield current
        else:
            try:
                iter(current)
            except TypeError:
                yield current
            else:
                stack.extend(reversed(current))


# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception


def map_like(fun: Callable[[Any], Any], *elems: Any) -> Iterator[Any]:
    """
    Map-like function
    :param fun: A function to apply to each element
    :param elems: Any number of elements of any type
    :return: Iterator yielding results (if arg function can't be applied - element as is + text exception are returned)
    """
    for elem in elems:
        try:
            yield fun(elem)
        except Exception as e:
            yield f"{elem}: {e}"


def main():
    # example input
    a = [1, 2, 3]
    b = 6
    c = "zhaba"
    d = [[1, 2], [3, 4]]
    e = {"a": 1, "b": 2}
    f = b"abc"
    g = bytearray(b"abc")

    for _ in merge_elems(a, b, c, d, e, f, g):
        print(_, end=" ")

    print("\n" + "-" * 70)

    # output: 1 2 3 6 z h a b a 1 2 3 4

    # example input
    a = [1, 2, 3]
    b = 6
    c = "zhaba"
    d = True
    e = {1: "a", 2: "b"}
    f = [(1, 2)]
    g = (6, 7, 8)
    h = 10.2
    i = b"abc"
    j = bytearray(b"dbd")
    k = lambda x: x[0] + 1
    fun = lambda x: x[0]

    for _ in map_like(fun, a, b, c, d, e, f, g, h, i, j, k):
        print(_)

    # output:
    # 1
    # 6: 'int' object is not subscriptable
    # z
    # True: 'bool' object is not subscriptable


if __name__ == "__main__":
    main()
