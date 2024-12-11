#!/usr/bin/env python

k = 18
m = 26
n = 30
total = (k + m + n)

probability = (
    (k / total) +
    ((m / total) * ((4 * k + 3 * m - 3 + 2 * n) / (4 * (total - 1)))) +
    ((n / total) * ((2 * k + m) / (2 * (total - 1))))
)
print(probability)