#!/usr/bin/env python

import itertools
import math
from pathlib import Path

with open(Path("i8.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()

instr = data[0]
data = data[2:]

dir_map = {"L": 0, "R": 1}

graph = {}
for line in data:
    src, dst = line.split(" = ")
    dst = dst[1:-1].split(", ")
    graph[src] = dst


def do1(start="AAA", end=lambda v: v == "ZZZ"):
    v = start
    for i, d in enumerate(itertools.cycle(instr)):
        v = graph[v][dir_map[d]]
        if end(v):
            return i + 1
    return -1


print(do1())


def do2():
    results = [
        do1(start=v, end=lambda v: v.endswith("Z")) for v in graph if v.endswith("A")
    ]

    return math.lcm(*results)


print(do2())
