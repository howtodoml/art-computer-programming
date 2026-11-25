"""TAOCP Vol. 1, 1.1-6: T_5, the average number of E1 steps when n = 5."""

from fractions import Fraction


def e1_count(m, n):
    count = 0
    while True:
        count += 1
        r = m % n
        if r == 0:
            return count
        m, n = n, r


def average_e1(n):
    return Fraction(sum(e1_count(m, n) for m in range(1, n + 1)), n)


def test_t5():
    counts = [e1_count(m, 5) for m in range(1, 6)]
    assert counts == [2, 3, 4, 3, 1]
    assert average_e1(5) == Fraction(13, 5)
    for m in range(1, 501):
        assert e1_count(m, 5) == e1_count((m - 1) % 5 + 1, 5)


if __name__ == "__main__":
    test_t5()
    print("T_5 =", average_e1(5), "=", float(average_e1(5)))
    print("1.1-6: all checks passed")
