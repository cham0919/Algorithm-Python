"""https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3"""
import math

mList = [
    4
]


nList = [
    3
]


puddlesList = [
    [[2, 2]]
]


returnList = [
    4
]


def solution(m, n, puddles):
    road = [[0 for j in range(n+1)] for i in range(m+1)]

    road[1][1] = 1

    for x, y in puddles:
        road[x][y] = -1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if road[i][j] == -1:
                road[i][j] = 0
                continue
            elif i != 1:
                road[i][j] = (road[i-1][j] + road[i][j-1]) % 1000000007
            elif j != 1:
                road[i][j] = road[i-1][j] + road[i][j-1] % 1000000007

    return road[m][n]


for m, n, p, r in zip(mList, nList, puddlesList, returnList):

    result = solution(m, n, p)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
