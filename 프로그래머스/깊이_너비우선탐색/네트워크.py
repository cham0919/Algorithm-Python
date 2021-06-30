"""https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3"""
from collections import defaultdict

nList = [
    3,
    3
]

computersList = [
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
]

returnList = [
    2,
    1
]


def dfs(computers, check, i):
    check[i] = True

    for j in range(len(computers)):
        if i != j and computers[i][j] == 1 and check[j] == False:
            dfs(computers, check, j)


def solution(n, computers):
    result = 0
    check = defaultdict(lambda: False)

    for i in range(n):
        if not check[i]:
            dfs(computers, check, i)
            result += 1

    return result


for n, c, r in zip(nList, computersList, returnList):

    result = solution(n, c)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
