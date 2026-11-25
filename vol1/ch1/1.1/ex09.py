"""TAOCP Vol. 1, 1.1-9: checking a simulation (g, h, j) of Algorithm E.

C1 is Algorithm E written as a computational method, in the spirit of Eqs. (2):
    (m, n)        -> (m, n, 0, 1)
    (m, n, r, 1)  -> (m, n, m mod n, 2)
    (m, n, r, 2)  -> (n,) if r == 0 else (m, n, r, 3)
    (m, n, r, 3)  -> (n, r, r, 1)
    (n,)          -> (n,)               output states

C2 is a small register machine with a program counter and registers M, N, R.
It has no division: it finds the remainder by repeated subtraction, so one
step of C1 can take many steps of C2. States are (pc, M, N, R).
"""

LIMIT = 25


def f1(x):
    if len(x) == 1:
        return x
    if len(x) == 2:
        m, n = x
        return (m, n, 0, 1)
    m, n, r, k = x
    if k == 1:
        return (m, n, m % n, 2)
    if k == 2:
        return (n,) if r == 0 else (m, n, r, 3)
    return (n, r, r, 1)


def f2(q):
    pc, M, N, R = q
    if pc == "S":
        return (0, M, N, 0)
    if pc == 0:
        return (1, M, N, M)
    if pc == 1:
        return (1, M, N, R - N) if R >= N else (2, M, N, R)
    if pc == 2:
        return ("H", M, N, R) if R == 0 else (3, M, N, R)
    if pc == 3:
        return (4, N, N, R)
    if pc == 4:
        return (0, M, R, R)
    return q


def in_omega1(x):
    return len(x) == 1


def in_omega2(q):
    return q[0] == "H"


def g(x):
    m, n = x
    return ("S", m, n, 0)


def h(q):
    pc, M, N, R = q
    if pc == "S":
        return (M, N)
    if pc in (0, 1):
        return (M, N, R, 1)
    if pc == 2:
        return (M, N, R, 2)
    if pc == 3:
        return (M, N, R, 3)
    if pc == 4:
        return (M, M, R, 3)
    return (N,)


def j(q):
    pc, M, N, R = q
    if pc == 0:
        return 1 + M // N + 1
    if pc == 1:
        return R // N + 1
    if pc == 3:
        return 2
    return 1


def iterate(f, q, k):
    for _ in range(k):
        q = f(q)
    return q


def reachable_states():
    seen = set()
    for m in range(1, LIMIT + 1):
        for n in range(1, LIMIT + 1):
            q = g((m, n))
            while q not in seen:
                seen.add(q)
                q = f2(q)
    return seen


def test_conditions():
    for m in range(1, LIMIT + 1):
        for n in range(1, LIMIT + 1):
            assert h(g((m, n))) == (m, n)
    for q in reachable_states():
        assert j(q) >= 1
        assert f1(h(q)) == h(iterate(f2, q, j(q))), q
        assert in_omega1(h(q)) == in_omega2(q), q


def test_mimics():
    for m in range(1, LIMIT + 1):
        for n in range(1, LIMIT + 1):
            x, q = (m, n), g((m, n))
            while True:
                assert h(q) == x
                if in_omega1(x):
                    assert in_omega2(q)
                    break
                q = iterate(f2, q, j(q))
                x = f1(x)
            assert x == (__import__("math").gcd(m, n),)


if __name__ == "__main__":
    test_conditions()
    test_mimics()
    print("1.1-9: all checks passed")
