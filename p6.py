#!/usr/bin/env python

import math
from pathlib import Path

with open(Path("i6.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()

ts = map(int, data[0].split()[1:])
xs = map(int, data[1].split()[1:])


def do1(t, x):
    # x < (t - hold_time) * hold_time
    # (t - sqrt(t**2 - 4*x))/2 < hold_time < (t + sqrt(t**2 - 4 *x))/2
    # |hold_times| = sqrt(t**2 - 4x)
    b = math.ceil((t - math.sqrt(t**2 - 4 * x)) / 2)
    e = math.floor((t + math.sqrt(t**2 - 4 * x)) / 2)
    res = e - b + 1
    if x == (t - b) * b:
        res -= 1
    if x == (t - e) * e:
        res -= 1
    return res


print(math.prod(do1(t, x) for t, x in zip(ts, xs)))


ts = map(int, data[0].split()[1:])
xs = map(int, data[1].split()[1:])


def do2():
    t = int(data[0].replace(" ", "").split(":")[-1])
    x = int(data[1].replace(" ", "").split(":")[-1])
    return do1(t, x)


print(do2())
