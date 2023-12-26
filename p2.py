#!/usr/bin/env python

from math import prod
from pathlib import Path

with open(Path("i2.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()


p1_limits = {"red": 12, "green": 13, "blue": 14}


def do1(line):
    game_number, game = line.split(": ")
    game_number = int(game_number.split(" ")[-1])
    list_of_sets = [s.split(", ") for s in game.split("; ")]
    for s in list_of_sets:
        counts = {}
        for c in s:
            count, color = c.split(" ")
            count = int(count)
            counts[color] = counts.get(color, 0) + count
        for color, number in counts.items():
            if p1_limits.get(color, 0) < int(number):
                return 0

    return game_number


print(sum(do1(line) for line in data))


def do2(line):
    p2_res = {}
    game_number, game = line.split(": ")
    game_number = int(game_number.split(" ")[-1])
    list_of_sets = [s.split(", ") for s in game.split("; ")]
    for s in list_of_sets:
        counts = {}
        for c in s:
            count, color = c.split(" ")
            count = int(count)
            counts[color] = counts.get(color, 0) + count
        for color, number in counts.items():
            if p2_res.get(color, 0) < int(number):
                p2_res[color] = int(number)

    return prod(p2_res.values())


print(sum(do2(line) for line in data))
