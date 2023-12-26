#!/usr/bin/env python

from pathlib import Path

with open(Path("in_1.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()


def do1(line):
    first, last = None, None
    for c in line:
        # print(c, c.isnumeric())
        if c.isnumeric():
            last = c
            if first is None:
                first = c
    if first is None or last is None:
        return 0
    return int(first + last)


print(sum(do1(line) for line in data))


def do2(line):
    replaces = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for word, digit in replaces.items():
        line = line.replace(word, f"{word}{digit}{word}")
    return do1(line)


print(sum(do2(line) for line in data))
