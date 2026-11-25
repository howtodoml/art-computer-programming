"""TAOCP Vol. 1, 1.1-8: an effective formal gcd algorithm on strings a^m b^n.

Each state j has (theta, phi, a, b). In state j, if theta occurs in the
string, its leftmost occurrence is replaced by phi and control goes to b;
otherwise the string is left alone and control goes to a. State N = 5 halts.
"""

import math

N = 5
TABLE = {
    0: ("ab", "", 2, 1),
    1: ("", "c", 0, 0),
    2: ("a", "b", 3, 2),
    3: ("c", "a", 4, 3),
    4: ("b", "b", 5, 0),
}


def run(sigma, limit=10**7):
    j, steps = 0, 0
    while j != N:
        theta, phi, a_j, b_j = TABLE[j]
        k = sigma.find(theta)
        if k < 0:
            j = a_j
        else:
            sigma = sigma[:k] + phi + sigma[k + len(theta):]
            j = b_j
        steps += 1
        assert steps < limit
    return sigma, steps


def test_gcd():
    for m in range(1, 61):
        for n in range(1, 61):
            out, _ = run("a" * m + "b" * n)
            assert out == "a" * math.gcd(m, n), (m, n, out)


def step(sigma, j):
    theta, phi, a_j, b_j = TABLE[j]
    k = sigma.find(theta)
    if k < 0:
        return sigma, a_j
    return sigma[:k] + phi + sigma[k + len(theta):], b_j


def test_one_round():
    sigma, j = "a" * 7 + "b" * 3, 0
    while j != 4:
        sigma, j = step(sigma, j)
    assert sigma == "aaa" + "bbbb"


if __name__ == "__main__":
    test_gcd()
    test_one_round()
    print("1.1-8: all checks passed")
