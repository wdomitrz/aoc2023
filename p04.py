#!/usr/bin/env python

from pathlib import Path

with open(Path("i04.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()


def count(line):
    _, line = line.split(": ")
    s1, s2 = line.split(" | ")
    s1, s2 = set(s1.split()), set(s2.split())
    s = s1 & s2
    return len(s)


def do1(line):
    r = count(line)
    if r == 0:
        return 0
    return 2 ** (r - 1)


print(sum(do1(line) for line in data))


def do2(data):
    counts = [1 for _ in data]
    for i, line in enumerate(data):
        r = count(line)
        for j in range(i + 1, i + r + 1):
            counts[j] += counts[i]
    return sum(counts)


print(do2(data))
