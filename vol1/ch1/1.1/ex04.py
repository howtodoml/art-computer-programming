"""TAOCP Vol. 1, 1.1-4: gcd(2166, 6099) by Algorithm E, with a trace."""

import math


def algorithm_e_trace(m, n):
    steps = []
    while True:
        q, r = divmod(m, n)
        steps.append((m, n, q, r))
        if r == 0:
            return n, steps
        m, n = n, r


def test_gcd():
    g, steps = algorithm_e_trace(2166, 6099)
    assert g == 57 == math.gcd(2166, 6099)
    assert len(steps) == 6
    assert 2166 == 57 * 38 and 6099 == 57 * 107
    assert math.gcd(38, 107) == 1


if __name__ == "__main__":
    test_gcd()
    g, steps = algorithm_e_trace(2166, 6099)
    for m, n, q, r in steps:
        print(f"{m} = {q} x {n} + {r}")
    print("1.1-4: all checks passed")
