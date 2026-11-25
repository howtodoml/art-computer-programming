"""TAOCP Vol. 1, 1.1-2: m > n at the start of E1 after the first pass."""

import math


def algorithm_e(m, n):
    first = True
    while True:
        if not first:
            assert m > n, (m, n)
        assert n > 0
        first = False
        r = m % n
        if r == 0:
            return n
        m, n = n, r


def test_invariant():
    for m in range(1, 201):
        for n in range(1, 201):
            assert algorithm_e(m, n) == math.gcd(m, n)


if __name__ == "__main__":
    test_invariant()
    print("1.1-2: all checks passed")
