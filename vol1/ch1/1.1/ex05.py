"""TAOCP Vol. 1, 1.1-5: the reading procedure has no stopping step.

The flowchart's arrows are encoded as edges between box numbers. An algorithm
must terminate, so somewhere there has to be a box with no way out. This
checks that there is none, and that box 18 leads straight back to box 3.
"""

EDGES = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [7, 6],
    6: [7, 16],
    7: [8, 16],
    8: [7, 9],
    9: [11, 10],
    10: [12],
    11: [12],
    12: [13],
    13: [12, 14],
    14: [15, 7],
    15: [7],
    16: [17],
    17: [4, 18],
    18: [3],
}


def reachable(start):
    seen, stack = set(), [start]
    while stack:
        v = stack.pop()
        if v not in seen:
            seen.add(v)
            stack.extend(EDGES[v])
    return seen


def test_no_halt():
    assert set(EDGES) == set(range(1, 19))
    assert all(EDGES[v] for v in EDGES), "some box has no exit"
    assert 3 in reachable(18)
    assert reachable(3) == set(range(3, 19))
    assert 12 in EDGES[13] and 13 in EDGES[12]


if __name__ == "__main__":
    test_no_halt()
    print("1.1-5: all checks passed")
