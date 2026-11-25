"""TAOCP Vol. 1, 1.1-7: U_m, the average E1 count over n with m fixed, equals T_m + 1."""

from fractions import Fraction


def e1_count(m, n):
    count = 0
    while True:
        count += 1
        r = m % n
        if r == 0:
            return count
        m, n = n, r


def T(n):
    return Fraction(sum(e1_count(m, n) for m in range(1, n + 1)), n)


def test_shift():
    for m in range(1, 41):
        for n in range(m + 1, m + 200):
            assert e1_count(m, n) == 1 + e1_count(n, m)


def test_block_average_is_exact():
    for m in range(1, 41):
        block = range(m + 1, 2 * m + 1)
        avg = Fraction(sum(e1_count(m, n) for n in block), m)
        assert avg == T(m) + 1, (m, avg, T(m) + 1)


def test_running_average_converges():
    for m in (1, 5, 12, 37):
        N = 200000
        avg = Fraction(sum(e1_count(m, n) for n in range(1, N + 1)), N)
        assert abs(avg - (T(m) + 1)) < Fraction(m * 10, N)


if __name__ == "__main__":
    test_shift()
    test_block_average_is_exact()
    test_running_average_converges()
    print("U_5 =", T(5) + 1)
    print("1.1-7: all checks passed")
