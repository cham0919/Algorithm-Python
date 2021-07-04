"""https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3"""
import math
from collections import defaultdict

nList = [
    6
]

edgeList = [
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
]

returnList = [
    3
]


def solution(n, edge):
    answer = 0
    path = [[False for row in range(n + 1)] for row in range(n + 1)]
    distince = [0 for row in range(n + 1)]


    for i, o in edge:
        path[i][o] = True
        path[o][i] = True

    maxVal = 0
    bfs = [1]
    while len(bfs) != 0:
        node = bfs.pop()

        for j in range(2, n+1, 1):
            if distince[j] == 0 and path[node][j]:
                distince[j] = distince[node] + 1
                bfs.append(j)
                maxVal = max(maxVal, distince[j])
                path[node][j] = path[j][node] = False

    for d in distince:
        if maxVal == d:
            answer += 1

    return answer

def solution2(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer

for n, e, r in zip(nList, edgeList, returnList):

    result = solution(n, e)

    if result == r:
        print("성공", result, r)
    else:
        print("실패", result, r)
