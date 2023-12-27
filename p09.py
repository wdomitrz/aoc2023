#!/usr/bin/env python

from pathlib import Path

with open(Path("i09.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()


def helper(curr_data):
    if curr_data == [0] * len(curr_data):
        return 0
    diffs = [y - x for x, y in zip(curr_data, curr_data[1:])]
    return curr_data[-1] + helper(diffs)


def do1(line):
    line = list(map(int, line.split()))
    return helper(line)


print(sum(do1(line) for line in data))


def helper2(curr_data):
    if curr_data == [0] * len(curr_data):
        return 0
    diffs = [y - x for x, y in zip(curr_data, curr_data[1:])]
    return curr_data[0] - helper2(diffs)


def do2(line):
    line = list(map(int, line.split()))
    return helper2(line)


print(sum(do2(line) for line in data))
