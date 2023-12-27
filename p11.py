#!/usr/bin/env python

import bisect
from pathlib import Path

with open(Path("i11.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()


def do1_and_2(cosmic_constant=2):
    galaxies = set()
    galaxies_x = set()
    galaxies_y = set()
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == "#":
                galaxies.add((x, y))
                galaxies_x.add(x)
                galaxies_y.add(y)

    galaxies_x = sorted(galaxies_x)
    galaxies_y = sorted(galaxies_y)

    new_galaxies = [
        (
            gx + (cosmic_constant - 1) * (gx - bisect.bisect_left(galaxies_x, gx)),
            gy + (cosmic_constant - 1) * (gy - bisect.bisect_left(galaxies_y, gy)),
        )
        for gx, gy in galaxies
    ]
    new_xs = sorted(gx for gx, _ in new_galaxies)
    new_ys = sorted(gy for _, gy in new_galaxies)

    def get_res_1d(coords_1d):
        res = 0
        prev_count = 0
        prev_loc = coords_1d[0]
        prev_dists = 0
        for c in coords_1d:
            prev_dists += prev_count * (c - prev_loc)
            res += prev_dists
            prev_count += 1
            prev_loc = c
        return res

    return get_res_1d(new_xs) + get_res_1d(new_ys)


print(do1_and_2(cosmic_constant=2))


print(do1_and_2(cosmic_constant=1000000))
