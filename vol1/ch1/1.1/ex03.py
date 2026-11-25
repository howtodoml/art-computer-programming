"""TAOCP Vol. 1, 1.1-3: Algorithm F, Euclid without the trivial replacements."""

import math


def algorithm_e(m, n):
    divisions = 0
    while True:
        r = m % n
        divisions += 1
        if r == 0:
            return n, divisions
        m, n = n, r


def algorithm_f(m, n):
    divisions = 0
    while True:
        m = m % n
        divisions += 1
        if m == 0:
            return n, divisions
        n = n % m
        divisions += 1
        if n == 0:
            return m, divisions


def test_f_matches_e():
    for m in range(1, 301):
        for n in range(1, 301):
            g_e, d_e = algorithm_e(m, n)
            g_f, d_f = algorithm_f(m, n)
            assert g_f == g_e == math.gcd(m, n), (m, n)
            assert d_f == d_e, (m, n, d_e, d_f)


if __name__ == "__main__":
    test_f_matches_e()
    print("1.1-3: all checks passed")
