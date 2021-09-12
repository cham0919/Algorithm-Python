"""https://www.acmicpc.net/problem/1931"""

import sys

N = int(sys.stdin.readline())
time = []

for _ in range(N):
    s,e = map(int, sys.stdin.readline().split())
    time.append([s,e])

time.sort(key= lambda x: (x[1], x[0]))


e = 0
result = 0

for lession in time:
    if lession[0] >= e:
        e = lession[1]
        result += 1

print(result)