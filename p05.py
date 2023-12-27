#!/usr/bin/env python

import bisect
import math
from pathlib import Path

with open(Path("i05.txt"), "r", encoding="utf8") as f:
    data = f.read().strip()

seeds = list(map(int, data.splitlines()[0].split(": ")[-1].split()))

mappings = [
    sorted(
        (t[1], t[0], t[2])
        for line in mapping.splitlines()[1:]
        for t in [tuple(map(int, line.split()))]
    )
    for mapping in data.split("\n\n")[1:]
]


def get_from_mapping(mapping, what):
    if len(mapping) == 0:
        return what, math.inf
    where = bisect.bisect(mapping, (what, math.inf)) - 1
    if where < 0:
        return what, mapping[where + 1][0] - what

    how_to_map = mapping[where]

    if what - how_to_map[0] + 1 > how_to_map[2]:
        if where == len(mapping) - 1:
            return what, math.inf
        return what, mapping[where + 1][0] - what

    return (
        what - how_to_map[0] + how_to_map[1],
        how_to_map[2] - (what - how_to_map[0]),
    )


def do1():
    current_seeds = list(seeds)
    for mapping in mappings:
        current_seeds = [get_from_mapping(mapping, s)[0] for s in current_seeds]
    return min(current_seeds)


print(do1())


def do2():
    current_seeds = []
    for start, count in zip(seeds[::2], seeds[1::2]):
        current_seeds.append((start, count))

    for mapping in mappings:
        new_seeds = []
        for start, count in current_seeds:
            while count > 0:
                dst, max_count = get_from_mapping(mapping, start)
                local_count = min(count, max_count)
                new_seeds.append((dst, local_count))
                start += local_count
                count -= local_count
        current_seeds = new_seeds
    return min(current_seeds)


print(do2()[0])
