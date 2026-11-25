"""TAOCP Vol. 1, 1.1-1: rotate (a, b, c, d) -> (b, c, d, a) in five replacements."""


def rotate(a, b, c, d):
    t = a
    a = b
    b = c
    c = d
    d = t
    return a, b, c, d


def test_rotate():
    assert rotate(1, 2, 3, 4) == (2, 3, 4, 1)
    assert rotate("w", "x", "y", "z") == ("x", "y", "z", "w")
    assert rotate(7, 7, 8, 8) == (7, 8, 8, 7)


if __name__ == "__main__":
    test_rotate()
    print("1.1-1: all checks passed")
