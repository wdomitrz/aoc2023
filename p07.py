#!/usr/bin/env python

import collections
from pathlib import Path

with open(Path("i07.txt"), "r", encoding="utf8") as f:
    data = f.read().strip().splitlines()

strength = "AKQJT98765432"


def to_key(hand, v=None):
    counts = collections.Counter(hand)
    hand_strengths = [-strength.index(c) for c in hand]
    res = sorted(counts.values(), reverse=True), hand_strengths
    if v is not None:
        return *res, v
    return res


def do1():
    res = 0
    for i, hand_res in enumerate(sorted((to_key(*line.split()) for line in data))):
        v = int(hand_res[-1])
        res += (i + 1) * v
    return res


print(do1())


strength2 = "AKQT98765432J"


def to_key2(hand, v=None):
    counts = collections.Counter(hand)
    hand_strengths = [-strength2.index(c) for c in hand]
    if counts["J"] != len(hand):
        count_j = counts["J"]
        counts["J"] = 0
        counts[counts.most_common(1)[0][0]] += count_j
    res = sorted(counts.values(), reverse=True), hand_strengths
    if v is not None:
        return *res, v
    return res


def do2():
    res = 0
    for i, hand_res in enumerate(sorted((to_key2(*line.split()) for line in data))):
        v = int(hand_res[-1])
        res += (i + 1) * v
    return res


print(do2())
