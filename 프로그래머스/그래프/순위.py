"""https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3"""

from collections import defaultdict

nList = [
    5
]

resultsList = [
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
]

returnList = [
    2
]


def mergeResultWin(a, target, check):
    for i in range(0, len(a), 1):
        if target[i] == 1 and a[i] != 1:
            a[i] = 1
            check = True
    return check


def mergeResultLose(a, target, check):
    for i in range(0, len(a), 1):
        if target[i] == -1 and a[i] != -1:
            a[i] = -1
            check = True
    return check


def checkReturnN(graph, n):
    count = 0
    for i in range(0, len(graph), 1):
        rCount = n - 1
        for j in range(0, len(graph[0]), 1):
            if graph[i][j] != 0:
                rCount -= 1
        if rCount == 0:
            count += 1
    return count


def solution(n, results):
    answer = 0
    graph = [[0 for i in range(n)] for i in range(n)]

    for start, end in results:
        graph[start - 1][end - 1] = 1
        graph[end - 1][start - 1] = -1

    check = True

    while check:
        check = False
        for start in range(0, n):
            for end in range(0, n):
                if graph[start][end] == 1:
                    check = mergeResultWin(graph[start], graph[end], check)
                elif graph[start][end] == -1:
                    check = mergeResultLose(graph[start], graph[end], check)

    return checkReturnN(graph, n)


def solution2(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer


for n, rl, r in zip(nList, resultsList, returnList):

    result = solution2(n, rl)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
