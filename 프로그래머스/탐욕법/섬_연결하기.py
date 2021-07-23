"""https://programmers.co.kr/learn/courses/30/lessons/42860"""
from collections import Counter

NList = [
    4
]

CostsList = [
    [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
]

returnList = [
    4
]


def find(node, parents):
    if parents[node] == node:
        return node
    else:
        return find(parents[node], parents)


def union(a, b, parents):
    rootA = find(a, parents)
    rootB = find(b, parents)

    if rootA != rootB:
        parents[rootB] = rootA


def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]

    for w, f, t in edges:
        if find(f, parents) == find(t, parents):
            continue
        else:
            union(f, t, parents)
            answer += w

    return answer


for n, c, r in zip(NList, CostsList, returnList):

    result = solution(n, c)

    if result == r:
        print("성공")
    else:
        print("실패")
