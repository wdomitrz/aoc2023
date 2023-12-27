#!/usr/bin/env python

from pathlib import Path

with open(Path("i10.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()

dirs = {
    n: vs | {(-o[0], -o[1]): (-i[0], -i[1]) for i, o in vs.items()}
    for n, vs in {
        "|": {(1, 0): (1, 0)},
        "-": {(0, 1): (0, 1)},
        "L": {(1, 0): (0, 1)},
        "J": {(1, 0): (0, -1)},
        "7": {(-1, 0): (0, -1)},
        "F": {(-1, 0): (0, 1)},
        ".": {},
        "S": {},
    }.items()
}


bg = (-1, -1)
for x, line in enumerate(data):
    for y, c in enumerate(line):
        if c == "S":
            bg = x, y


def go(x, y, how, steps):
    while data[x][y] != "S":
        if how not in dirs[data[x][y]]:
            return None
        dx, dy = dirs[data[x][y]][how]
        x, y, how, steps = x + dx, y + dy, (dx, dy), steps + 1
    return steps


def do1():
    for sx, sy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r = go(bg[0] + sx, bg[1] + sy, how=(sx, sy), steps=1)
        if r is not None:
            return (r + 1) // 2, (sx, sy)
    return -1, None


print(do1()[0])


def do2():
    initial_move = do1()[1]

    def get_blocked(x, y, how):
        blocked = set()
        while data[x][y] != "S":
            blocked.add((x, y))
            dx, dy = dirs[data[x][y]][how]
            x, y, how = x + dx, y + dy, (dx, dy)
        blocked.add((x, y))
        return blocked

    blocked = get_blocked(
        bg[0] + initial_move[0],
        bg[1] + initial_move[1],
        how=(initial_move[0], initial_move[1]),
    )

    res = 0
    for x, line in enumerate(data):
        is_outer = True
        init = None
        for y, c in enumerate(line):
            if (x, y) in blocked:
                if c in "|":
                    is_outer = not is_outer
                elif c in "FL":
                    init = c
                elif c in "7J":
                    if c == "7" and init == "L":
                        is_outer = not is_outer
                    elif c == "J" and init == "F":
                        is_outer = not is_outer
                    init = None
            elif (x, y) not in blocked:
                if not is_outer:
                    res += 1

    return res


print(do2())
