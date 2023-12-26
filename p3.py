#!/usr/bin/env python

from math import prod
from pathlib import Path

with open(Path("i3.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()


def is_ok(x, y):
    def helper(px, py, forbidden_symbols=".0123456789"):
        if not 0 <= px < len(data):
            return False
        if not 0 <= py < len(data[px]):
            return False
        return data[px][py] not in forbidden_symbols

    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            if helper(x + px, y + py):
                return True

    return False


def do1(data):
    res = 0
    for i, line in enumerate(data):
        ok = False
        number = ""
        for j, c in enumerate(line):
            if c.isnumeric():
                number += c
                ok |= is_ok(i, j)
            else:
                if ok:
                    res += int(number)
                ok = False
                number = ""
        if ok:
            res += int(number)
    return res


print(do1(data))


def is_ok2(x, y):
    def helper(px, py):
        if not 0 <= px < len(data):
            return False
        if not 0 <= py < len(data[px]):
            return False
        return data[px][py] == "*"

    res = set()
    for px in [-1, 0, 1]:
        for py in [-1, 0, 1]:
            if helper(x + px, y + py):
                res.add((x + px, y + py))

    return res


def do2(data):
    p_res = {}
    for i, line in enumerate(data):
        oks = set()
        number = ""
        for j, c in enumerate(line):
            if c.isnumeric():
                number += c
                oks |= is_ok2(i, j)
            else:
                for ok in set(oks):
                    p_res[ok] = p_res.get(ok, []) + [int(number)]
                oks = set()
                number = ""
        for ok in oks:
            p_res[ok] = p_res.get(ok, []) + [int(number)]
    res = 0
    for a in p_res.values():
        if len(a) == 2:
            res += prod(a)
    return res


print(do2(data))
